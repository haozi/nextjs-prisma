#!/bin/bash
set -e
cd "$(dirname "$0")" || exit 1
cd ..

./Node.js/node_modules/.bin/concurrently \
  "cd ./Node.js/ && pnpm run lint && cd .." \
  "isort --profile black . && black ."
