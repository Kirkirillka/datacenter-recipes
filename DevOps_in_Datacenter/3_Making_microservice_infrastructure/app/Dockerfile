FROM python:3.9.0a5-buster as build-stage

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 9000 9000

ENTRYPOINT python3 run.py