#!/bin/bash
set -e
cd "$(dirname "$0")" || exit 1
cd ..

cd ./Node.js/ && pnpm install && cd ..

docker compose -f ./config/docker-compose.dev.yml -f ./config/docker-compose.dev.override.yml down
docker compose -f ./config/docker-compose.dev.yml -f ./config/docker-compose.dev.override.yml pull
docker image prune -f
