FROM python:3.12-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev build-base libffi-dev openssl-dev

COPY requirements.txt /temp/requirements.txt
RUN pip install --no-cache-dir -r /temp/requirements.txt

COPY . /book_club
WORKDIR /book_club

RUN mkdir -p /book_club/static
RUN chmod 755 /book_club/static

RUN adduser -D book_club
USER book_club

EXPOSE 80

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput  && daphne -b 0.0.0.0 -p 80 club.asgi:application"]
