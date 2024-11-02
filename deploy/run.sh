#!/bin/bash

docker compose up --detach

cmd.exe /C start wsl.exe -e /bin/bash -c "python3 ../source/console.py; bash exec"

#trap "docker compose down" EXIT