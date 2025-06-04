#!/bin/bash
set -e
cd "$(dirname "$0")" || exit 1
cd ..

python3 ./scripts/backup.py
