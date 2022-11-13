{ sources ? import ./nix/sources.nix 
, pkgs ? import sources.nixpkgs {}
}:
with pkgs;
mkShell {
    buildInputs = [
        python310
        python310Packages.pip
        python310Packages.pip-tools
    ];
    shellHook = ''
    pip-compile
    alias dc='docker compose'
    echo "Use handy aliases:"
    echo "* 'dc' for 'docker compose'"
    '';
}