# Pull the official base image
FROM python:3.12.0

# Set the working directory inside the container
WORKDIR /usr/src/app

# Set environment variables to prevent Python from writing bytecode and buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define arguments for setting secret key and DSN (Data Source Name)
ARG SECRET_KEY
ARG DSN

# Set environment variables using the provided arguments
ENV SECRET_KEY=${env.SECRET_KEY}
ENV DSN=${env.DSN}

# Expose port 8000 to the outside world
ENV PORT 8000
EXPOSE 8000

# Upgrade pip and copy requirements file to the working directory
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Collect static files
RUN python manage.py collectstatic --noinput

# Command to run the application using Gunicorn
CMD gunicorn --bind 0.0.0.0:$PORT oc_lettings_site.wsgi
