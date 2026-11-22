#!/bin/sh
set -eu
cd "$(dirname "$0")/../.."

runner=$(nix-build --no-out-link -E 'with import <nixpkgs> {}; callPackage ./agent-test {}')
python=$(nix-build --no-out-link -E 'with import <nixpkgs> {}; python3.withPackages (p: [ p.pytest p.pytest-xdist p.pyyaml ])')
export AGENT_TEST_BIN="$runner/bin/run" PYTHONDONTWRITEBYTECODE=1
exec "$python/bin/python" -m pytest -q -p no:cacheprovider --dist worksteal \
  --max-worker-restart=0 -n "${1:-4}" agent-test/tests
