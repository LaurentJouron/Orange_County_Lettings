FROM python:3.12.2-bullseye

WORKDIR /app

COPY ./requirements.txt /app

ENTRYPOINT [ "manage.py" ]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG SECRET_KEY
ARG DSN

ENV SECRET_KEY=${SECRET_KEY}
ENV DSN=${DSN}

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000