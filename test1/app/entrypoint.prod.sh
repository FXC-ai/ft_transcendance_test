#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."


    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py migrate --noinput
python manage.py collectstatic --no-input --clear

# the command specified in the Dockerfile's CMD instruction or the command in a docker-compose.yml.
exec "$@"