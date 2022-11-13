{ sources ? import ./nix/sources.nix 
, pkgs ? import sources.nixpkgs {}
}:
with pkgs;
mkShell {
    buildInputs = [
        python39
        python39Packages.pip
        python39Packages.pip-tools
        python39Packages.pip-tools
    ];
    shellHook = ''
    pip-compile
    alias dc='docker compose'
    alias pip='python -m pip'
    echo "Use handy aliases:"
    echo "* 'dc' for 'docker compose'"

    if [ -d "./.venv" ]
    then
        echo "Virtual environment (./.venv) exist."
        source .venv/bin/activate
    else
        echo "Virtual environment (./.venv) does not exist."
        echo "Creating a new one..."
        python -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    fi
    '';
}