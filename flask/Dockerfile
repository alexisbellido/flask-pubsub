FROM python:3.7.6-slim-buster as builder

WORKDIR /code

RUN set -e \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libomp-dev \
    libgomp1

RUN apt-get purge -y build-essential \
  && apt-get purge -y python3-dev \
  && apt-get autoremove -y \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

ENV REDIS_HOST 0.0.0.0
ENV REDIS_PORT 6379

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT=5000

COPY . .
ENTRYPOINT ["/code/docker-entrypoint.sh"]