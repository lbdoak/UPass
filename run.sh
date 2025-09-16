#!/bin/bash

source .venv/bin/activate

cd deploy

docker compose up --detach

cmd.exe /C start wsl.exe -e /bin/bash -c "python3 ../source/console.py; bash exec"