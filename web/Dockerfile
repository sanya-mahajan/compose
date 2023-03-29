FROM python:3.9.7-slim 
COPY . /app
WORKDIR /app


RUN python3 -m venv /opt/venv
#/opt for such stuff
RUN  /opt/venv/bin/pip install pip --upgrade && \
 /opt/venv/bin/pip  install -r requirements.txt && \
 chmod +x entrypoint.sh 

CMD ["/app/entrypoint.sh"]
#NEVER NEED TO ACTIVATE VENV

#use gunicorn in prod instead of manage.py runserver, hence the entrypoint.sh
#dont have accesss to migrate, createsuperuser so cant run migrate.sh



