# Advent of Code

This is a repository dedicated to the Advent of Code challenges.

## Developer setup: virtual environment

Set up a Python virtual environment (recommended path `.venv`) and install development dependencies:

PowerShell (Windows):

    scripts\setup_venv.ps1

Bash (Linux/macOS):

    ./scripts/setup_venv.sh

After creating the venv activate it, e.g. (PowerShell):

    .\.venv\Scripts\Activate.ps1

You can then run tests with `pytest` and other dev commands. The project provides `requirements-dev.txt` for dev-only dependencies.
