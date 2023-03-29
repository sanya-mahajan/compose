#! /bin/bash
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"sanyamahajan08@gmail.com" }
cd /app/  #manage.py is in /app/

/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createsuperuser --noinput --email ${DJANGO_SUPERUSER_EMAIL} || true #duplicate email error is ignored