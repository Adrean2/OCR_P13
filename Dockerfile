FROM python:3.8

WORKDIR /app
COPY requirements.txt .

ENV PYTHONDONTWRITEBYTCODE=1
ENV PYTHONUNBUFFERED=1

ARG SECRET_KEY=secret_key_dummy
ENV SECRET_KEY=${"SECRET_KEY"}

ARG SENTRY_DSN=sentry_dns_dummy
ENV SENTRY_DSN=${"SENTRY_DSN"}

RUN pip install -r requirements.txt
COPY . /app

RUN python manage.py collectstatic --noinput
#EXPOSE 8000
CMD gunicorn oc_lettings_site.wsgi -b 0.0.0.0$PORT


