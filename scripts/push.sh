#!/bin/bash
set -e

docker compose -f ./config/docker-compose.prod.yml push
