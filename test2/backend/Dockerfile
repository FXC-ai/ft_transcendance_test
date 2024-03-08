FROM python:3.11.4-slim-buster as builder

WORKDIR /usr/src/bck_django

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

RUN pip install --upgrade pip

RUN pip install django
RUN pip install gunicorn

RUN pip wheel --no-cache-dir --no-deps --wheel-dir wheels psycopg2-binary


RUN addgroup --system bck_django && adduser --system --group bck_django

RUN chown -R bck_django:bck_django /usr/src/bck_django

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "bck_django.wsgi"]