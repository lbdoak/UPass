#!/bin/bash

python3 -m venv .venv

source .venv/bin/activate

pip3 install -r requirements.txt

echo "Setup complete. PassMan is ready to run with "bash run.sh""