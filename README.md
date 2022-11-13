# Twts - timeseries API

## Init dev environment

1. Install (Nix package manager)[https://nixos.org/download.html].
1. Run nix shell to start using proper version of Python:
    ```
    nix-shell
    ```
1. Instantiate Python virtual environment:
    ```bash
    python3.10 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```

## Run tests

```bash
nox -s test
```