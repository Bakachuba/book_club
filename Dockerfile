FROM python:3.12-alpine3.18

RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN apk add --no-cache build-base libffi-dev openssl-dev

COPY requirements.txt /temp/requirements.txt
RUN pip install --no-cache-dir -r /temp/requirements.txt

COPY . /book_club
WORKDIR /book_club

RUN adduser --disabled-password book-user
USER book-user

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "club.asgi:application"]
