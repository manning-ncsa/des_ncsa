#!/bin/bash


if [[ -z "$DR_SERVER_URL" ]]; then
    DR_SERVER_URL=desdr-server.ncsa.illinois.edu
fi

set -euo pipefail

find static/des_components -type f -exec sed -i "s/{{drserverbaseurl}}/${DR_SERVER_URL}/g" {} \;

python main.py
