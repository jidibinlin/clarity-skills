{ runCommand, python3 }:
let
  python = python3.withPackages (ps: [ ps.pyyaml ]);
in
runCommand "clarity-agent-test" { } ''
  private="$out/libexec/agent-test"
  extensions="$out/share/agent-test"
  mkdir -p "$out/bin" "$private" "$extensions"
  install_program() {
    printf '#!%s -Es\n' '${python}/bin/python3' > "$2"
    cat "$1" >> "$2"
    chmod 755 "$2"
  }
  install_program ${./src/submit.py} "$private/submit.py"
  install_program ${./src/supervise.py} "$private/supervise"
  cp ${./src/materials.py} "$private/materials.py"
  cp ${./omp/main-session.ts} "$extensions/main-session.ts"
  cp ${./omp/coordinator.ts} "$extensions/coordinator.ts"
  cp ${./omp/locked.yml} "$extensions/locked.yml"
  ln -s ../libexec/agent-test/submit.py "$out/bin/run"
''
