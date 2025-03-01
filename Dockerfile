FROM python:3.9
WORKDIR /usr/local/src/deepface

# RUN python -m venv .venv
# RUN source .venv/bin/activate
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

ADD requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src