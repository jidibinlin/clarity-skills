{ config, lib, pkgs, ... }:

let
  cfg = config.programs.clarityPlugins;
  package = pkgs.callPackage ./default.nix { };
in
{
  options.programs.clarityPlugins.enable = lib.mkEnableOption "Clarity communication rules for OMP, OpenCode and Codex";

  config = lib.mkIf cfg.enable {
    home.file.".omp/agent/extensions/clarity.js".source = "${package}/omp.js";
    home.file.".config/opencode/plugins/clarity.js".source = "${package}/opencode.js";
    home.file.".codex/AGENTS.md".text = lib.mkAfter (
      "\n" + builtins.readFile ../rules/communication-style.md
    );
  };
}
