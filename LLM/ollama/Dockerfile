FROM python:3.13-slim

RUN apt-get update && \
    \
    apt-get install -y --no-install-recommends curl && \
    curl -fsSL https://ollama.com/install.sh | sh && \
    \
    apt-get clean && rm -rf /var/lib/apt/lists/*
