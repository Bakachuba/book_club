FROM python:3.12-alpine3.18

RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN apk add build-base libffi-dev openssl-dev

COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt

COPY . /book_club
WORKDIR /book_club

RUN adduser --disabled-password book-user
USER book-user

RUN python manage.py makemigrations
RUN python manage.py migrate

COPY . .
RUN python manage.py collectstatic --noinput

RUN python manage.py createsuperuser --noinput --username admin --email admin@example.com --password qawsed12 && \
    python manage.py createsuperuser --noinput --username first --email first@example.com --password qawsed12

EXPOSE 8000

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "club.asgi:application"]
