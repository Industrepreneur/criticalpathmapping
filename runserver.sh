#!/usr/bin/env bash

APP_ENV=${APP_ENV:-"production"}
DEVMODE=`[[ $APP_ENV == "dev" || $APP_ENV == "local" ]] && echo 1`
APP_DIR=`[[ -n $DEVMODE ]] && echo "/app-local" || echo "/app"`

cd "$APP_DIR"
sleep 2

printf "\n-----> Installing NodeJS dependencies...\n"
npm install

printf "\n-----> Installing Bower dependencies...\n"
bower install --allow-root


printf "\n-----> Bootstrapping ${APP_ENV} environment...\n"


printf "\n-----> Checking for DB Migrations...\n"
envdir envs/${APP_ENV} python3 manage.py makemigrations --noinput


printf "\n-----> Syncing DB Entries...\n"
envdir envs/${APP_ENV} python3 manage.py migrate --noinput


printf "\n-----> Loading Fixtures...\n"
envdir envs/${APP_ENV} python3 manage.py loaddata ${APP_ENV}


if [[ $DEVMODE == "1" ]]; then
    printf "\n-----> Starting the development server. Hack away!\n"
    while true; do sleep 2; envdir envs/${APP_ENV} python3 manage.py runserver_plus 0.0.0.0:8080; done
else
    printf "\n-----> Collecting static...\n"
    while [ $# -ne 0 ]; do
        if [ $1 == "--clear" ]; then CLEAR="--clear"; break; fi
        shift
    done
    envdir envs/${APP_ENV} python3 manage.py collectstatic ${CLEAR} --noinput

    printf "\n-----> Starting the production server.\n"
    envdir envs/${APP_ENV} gunicorn --bind 0.0.0.0:8080 mapping.wsgi
fi
