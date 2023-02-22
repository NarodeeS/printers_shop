FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . ./app

WORKDIR /app

RUN apt-get update -y && \
    apt-get upgrade -y && \
    pip3 install -r requirements.txt
