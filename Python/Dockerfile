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
        "uvicorn" \
        "gunicorn" \
        "fastapi-users[sqlalchemy]" \
        "fastapi-users[oauth]" \
        "fastapi[standard]" \
        \
        \
        && \
    pip cache purge

RUN pip install --root-user-action=ignore --no-cache-dir -r requirements.txt && \
    pip cache purge

# EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers $(python -c "import multiprocessing; print(min(2, multiprocessing.cpu_count() * 2))")
