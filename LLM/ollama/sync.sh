latest_version=0.6.2

docker pull ollama/ollama:latest


docker tag ollama/ollama:latest ghcr.io/haozi/ollama:dev-latest
docker tag ollama/ollama:latest ghcr.io/haozi/ollama:latest
docker tag ollama/ollama:latest ghcr.io/haozi/ollama:$latest_version

docker tag ollama/ollama:latest registry.cn-hangzhou.aliyuncs.com/psy-system/ollama:dev-latest
docker tag ollama/ollama:latest registry.cn-hangzhou.aliyuncs.com/psy-system/ollama:latest
docker tag ollama/ollama:latest registry.cn-hangzhou.aliyuncs.com/psy-system/ollama:$latest_version


docker push ghcr.io/haozi/ollama:dev-latest && \
docker push ghcr.io/haozi/ollama:latest && \
docker push ghcr.io/haozi/ollama:$latest_version &

docker push registry.cn-hangzhou.aliyuncs.com/psy-system/ollama:dev-latest && \
docker push registry.cn-hangzhou.aliyuncs.com/psy-system/ollama:latest && \
docker push registry.cn-hangzhou.aliyuncs.com/psy-system/ollama:$latest_version
