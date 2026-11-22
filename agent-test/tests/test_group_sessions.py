"""Four interactive OMP instances share one workspace. Only the model is scripted."""

import os
import pty
import re
import shutil
import signal
import subprocess
import threading
import unittest
from contextlib import ExitStack, contextmanager

import test_run
from provider import Dialogue, PEER, Reply, finish, read_tool, send


@contextmanager
def designer(h, run, name):
    profiles = run / 'home/.omp/profiles'
    agent = profiles / name / 'agent'
    agent.mkdir(parents=True)
    for file in ('config.yml', 'models.yml'):
        shutil.copy(profiles / 'subject/agent' / file, agent / file)
    def stop(proc):
        try:
            if proc.poll() is None:
                os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        proc.wait(timeout=5)

    def drain(master):
        try:
            while os.read(master, 65536):
                pass
        except OSError:  # Linux PTY hangs up when the last slave closes.
            pass

    with ExitStack() as resources:
        master, slave = pty.openpty()
        resources.callback(os.close, master)
        with os.fdopen(slave, 'rb', buffering=0) as tty:
            reader = threading.Thread(target=drain, args=(master,), daemon=True)
            reader.start()
            resources.callback(reader.join, 5)
            proc = subprocess.Popen(
                [h.omp, '--profile', name, '--model', 'beta/desk-groups', '--no-title',
                 '--config', test_run.PACKAGE / 'omp/locked.yml'],
                cwd=run / 'workspace', start_new_session=True,
                env={**h.env, 'HOME': str(run / 'home'), 'TMPDIR': str(run), 'BETA_KEY': h.b.key},
                stdin=tty, stdout=tty, stderr=tty,
            )
            resources.callback(stop, proc)
        yield proc.pid


def roster(d):
    reads = d.results_for('read', path='agent://peers')
    return PEER.findall(reads[-1]) if reads else []


def owner(d):
    if d.results_for('finish_run'):
        return Reply('text', 'Design conversations finished.')
    others = roster(d)
    if not d.verified_peer or len(others) != 3:
        if d.results_for('read', path='agent://peers', this_turn=True):
            return Reply('text', 'Awaiting the participants.')
        return read_tool('agent://peers')
    lead = d.verified_peer
    if not d.sent('Open the design'):
        # An attempted opening isn't a delivery: OMP refuses empty peer messages.
        if not d.results_for('write', path=f'agent://{lead}'):
            return send(lead, '')
        other = next(pid for pid in others if pid != lead)
        if not d.results_for('write', path=f'agent://{other}'):
            return send(other, 'Premature opening')
        if d.sent('Premature opening'):
            return finish('scenario_error', 'The opening reached the wrong participant.')
        return send(lead, 'Open the design')
    assignment = next((re.fullmatch(r'Groups: agent://(\d+) agent://(\d+)', msg)
                       for pid, msg in d.incoming if pid == lead and msg.startswith('Groups:')), None)
    if not assignment:
        return Reply('text', 'Awaiting the design lead.')
    for name, pid in zip(('A', 'B'), assignment.groups()):
        if not d.sent('Open group ' + name):
            if any(args.get('content') == 'Open group ' + name for _, _, args, _ in d.results):
                return finish('scenario_error', f'Could not contact group {name}.')
            return send(pid, 'Open group ' + name)
    if all((pid, f'Group {name} ready') in d.incoming
           for name, pid in zip(('A', 'B'), assignment.groups())):
        return finish('completed', 'Both group owners replied directly.')
    return Reply('text', 'Awaiting both designers.')


def participant(d):
    for sender, msg in d.incoming:
        if msg == 'Open the design':
            if not roster(d):
                return read_tool('agent://peers')
            groups = [pid for pid in roster(d) if pid != sender]
            if len(groups) == 2 and not d.sent('Groups:'):
                return send(sender, 'Groups: ' + ' '.join('agent://' + pid for pid in groups))
        elif msg in ('Open group A', 'Open group B') and not d.sent('Group '):
            return send(sender, f'Group {msg[-1]} ready')
    return Reply('text', 'Awaiting my assignment.')


class GroupSessionsTests(unittest.TestCase):
    def test_first_delivery_goes_to_lead_then_both_designers_can_reply_directly(self):
        h = test_run.RunTests()
        h.setUpClass()
        h.setUp()
        self.addCleanup(h.doCleanups)
        h.version(case='groups')
        for endpoint, turn in ((h.a, owner), (h.b, participant)):
            original = endpoint.respond

            def respond(request, authorized, turn=turn, original=original):
                d = Dialogue(request)
                if authorized and {'read', 'write'} <= d.tools:
                    return turn(d)
                return original(request, authorized)

            endpoint.respond = respond
        run = h.submit()
        with designer(h, run, 'design-a'), designer(h, run, 'design-b'):
            end = h.terminal(run)
            self.assertEqual(end['scene'], 'completed', end)
            h.assert_normal_teardown(run, end)
            for role in ('design-a', 'design-b'):
                entries = [e for p in h.sessions(run, role) for e in test_run.json_lines(p)]
                self.assertTrue(any(e['type'] == 'session' and not e.get('parentSession') for e in entries))
                messages = [e['details']['message'] for e in entries if e.get('customType') == 'irc:incoming']
                self.assertNotIn('Premature opening', messages)
                self.assertTrue(any(msg.startswith('Open group ') for msg in messages), messages)
