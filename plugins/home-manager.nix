{ config, lib, pkgs, ... }:

let
  cfg = config.programs.clarityPlugins;
  package = pkgs.callPackage ./default.nix { };
in
{
  options.programs.clarityPlugins.enable = lib.mkEnableOption "Clarity communication-style plugins for OMP and OpenCode";

  config = lib.mkIf cfg.enable {
    home.file.".omp/agent/extensions/clarity.js".source = "${package}/omp.js";
    home.file.".config/opencode/plugins/clarity.js".source = "${package}/opencode.js";
  };
}
