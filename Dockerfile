FROM python:3.12-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev build-base libffi-dev openssl-dev

COPY requirements.txt /temp/requirements.txt
RUN pip install --no-cache-dir -r /temp/requirements.txt

COPY . /book_club
WORKDIR /book_club

RUN adduser -D book_club
USER book_club

EXPOSE 8000

