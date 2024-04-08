FROM python:3.12-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

RUN apk add --no-cache build-base libffi-dev openssl-dev

COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt

WORKDIR /book_club

RUN adduser -D book_club && chmod 777 /opt /run

RUN mkdir /book_club/static && chown -R book_club:book_club /book_club && chmod 755 /book_club

COPY --chown=book_club:book_club . .

USER book_club

EXPOSE 80

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput  && daphne -b 0.0.0.0 -p 80 club.asgi:application"]
