FROM python:3.10.4-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

COPY . .

ARG name

RUN apk update \
    && apk add --virtual build-deps \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps

RUN pip install --upgrade pip

RUN pip install -r requirements.txt