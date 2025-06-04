#!/bin/bash

# 生产环境启动脚本
set -e

# docker compose -f ./config/docker-compose.prod.yml pull || true
# docker compose -f ./config/docker-compose.prod.yml build

docker compose -f ./config/docker-compose.prod.yml up \
  -d \
  --force-recreate \
  --no-build
