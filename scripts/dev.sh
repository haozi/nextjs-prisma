#!/bin/bash
set -e
cd "$(dirname "$0")" || exit 1
cd ..

# 生成 localhost 证书，请先安装 mkcert
mkcert -install
mkdir -p ./keys && mkcert \
  -cert-file ./keys/localhost.cert.pem \
  -key-file ./keys/localhost.key.pem \
  localhost 127.0.0.1 ::1

# lsof -t -i :65173 -i :63000 | xargs kill -9

./Node.js/node_modules/.bin/concurrently \
  "docker compose -f ./config/docker-compose.dev.yml -f ./config/docker-compose.dev.override.yml up" \
  "cd ./Node.js/ && pnpm run dev" \
  "sh ./scripts/lint.sh" \
  "sleep 5 && open https://localhost:9999/"
