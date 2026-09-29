FROM python:3.14-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src

COPY entrypoint.py .
COPY app/ app/

# Absolute path: the runner overrides WORKDIR with /github/workspace.
ENTRYPOINT ["python3", "/usr/src/entrypoint.py"]