FROM python:3.10.11-alpine3.17

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt && pip install psycopg2-binary

WORKDIR /app/src

EXPOSE 8000