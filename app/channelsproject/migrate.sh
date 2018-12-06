#!/bin/sh
sleep 2
python manage.py makemigrations notifier backend;
python manage.py migrate;