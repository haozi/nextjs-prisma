#!/bin/bash
set -e

SKIP_BUILD=false
for arg in "$@"; do
  if [ "$arg" == "--skip-build-app-i" ]; then
    SKIP_BUILD=true
  fi
done

if [ "$SKIP_BUILD" == "false" ]; then
  cd ./Node.js/ && pnpm run build && cd ..
fi

# docker compose -f ./config/docker-compose.prod.yml build
  # --no-cache
