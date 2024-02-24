# pull the official base image
FROM python:3.12.0

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG SECRET_KEY
ARG DSN
ENV SECRET_KEY=${SECRET_KEY}
ENV DSN=${DSN}

ENV PORT 8000

RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY . /usr/src/app

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD gunicorn --bind 0.0.0.0:$PORT oc_lettings_site.wsgi