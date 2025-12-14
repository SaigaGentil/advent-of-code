#!/usr/bin/env bash
set -euo pipefail
VENV_PATH=${1:-.venv}
python -m venv "$VENV_PATH"
"$VENV_PATH/bin/python" -m pip install --upgrade pip
if [ -f requirements-dev.txt ]; then
  "$VENV_PATH/bin/python" -m pip install -r requirements-dev.txt
fi
cat <<EOF
Virtual environment created at $VENV_PATH
Activate with:
  source $VENV_PATH/bin/activate
EOF