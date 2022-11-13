{ sources ? import ./nix/sources.nix 
, pkgs ? import sources.nixpkgs {}
}:
with pkgs;
mkShell {
    buildInputs = [
        python39
        python39Packages.pip
        python39Packages.pip-tools
    ];
    shellHook = ''
    echo "Running pip-compile..."
    pip-compile

    echo "Setting environment..."
    export PYTHONPATH="./src:$PYTHONPATH"

    echo "Setting aliases..."
    alias dc='docker compose'
    alias pip='python -m pip'
    alias ut='pytest src'
    alias run='python src/twts_api/main.py'
    echo "* 'dc' for 'docker compose'"
    echo "* 'pip' for 'python -m pip'"
    echo "* 'ut' to run tests with pytest"
    echo "* 'run' to run the API"

    if [ -d "./.venv" ]
    then
        echo "Virtual environment (./.venv) exist."
        source .venv/bin/activate
    else
        echo "Virtual environment (./.venv) does not exist."
        echo "Creating a new one..."
        python -m venv .venv
    fi
    source .venv/bin/activate
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    '';
}