#!/usr/bin/env bash

set -x
set -a

docker compose down --remove-orphans && \
    docker compose build && \
    docker compose run deepface