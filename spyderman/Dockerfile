FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN apt-get update && \
    \
    \
    apt-get install -y --no-install-recommends curl && apt-get clean && rm -rf /var/lib/apt/lists/* && \
    \
    \
    pip cache purge && pip install --upgrade pip && \
    pip install --root-user-action=ignore --no-cache-dir \
        "browser-use" \
        \
        \ && \
    pip install playwright && \
    playwright install && \
    \
    pip cache purge
