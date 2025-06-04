#!/bin/bash
set -e

docker compose -f ./config/docker-compose.prod.yml pull
docker compose -f ./config/docker-compose.dev.yml down
sh scripts/prod.start.sh
docker image prune -f

# docker service update --image your-app-image:new-tag my-app_app
