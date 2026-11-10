{ lib, runCommand, bun }:

let
  source = lib.fileset.toSource {
    root = ../.;
    fileset = lib.fileset.unions [
      ./build.mjs
      ./package.json
      ./shared
      ./omp
      ./opencode
      ./tests
      ../rules/communication-style.md
    ];
  };
in
runCommand "clarity-communication-plugins" { nativeBuildInputs = [ bun ]; } ''
  export HOME="$TMPDIR"
  cd ${source}
  bun plugins/build.mjs "$out"
  CLARITY_PLUGIN_BUILD="$out" bun test plugins/tests
''
