.. _docker:

**Docker**
==========

.. important::

    .. image:: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
        :alt: Docker Badge
        :target: https://www.sqlite.org/index.html

    Parameterizations are done to a specific project. To parameterize to the other project, go to the official 
    documentation `Docker <https://docs.docker.com/>`_.


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

=====================
Dockerfile for Python
=====================

This Docker file is used to build a Python application container.

💡 Pull the official base image

.. code-block:: console

    FROM python:3.12.0

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

💡 Set the working directory inside the container

.. code-block:: console

    WORKDIR /usr/src/app

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

💡 Set environment variables to prevent Python from writing bytecode and buffering stdout and stderr

.. code-block:: console

    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

💡 Define arguments for setting secret key and DSN (Data Source Name)

.. code-block:: console

    ARG SECRET_KEY
    ARG DSN

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

💡 Set environment variables using the provided arguments

.. code-block:: console

    ENV SECRET_KEY=${SECRET_KEY}
    ENV DSN=${DSN}

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

💡 Expose port 8000 to the outside world

.. code-block:: console

    ENV PORT 8000
    EXPOSE 8000

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

💡 Upgrade pip and copy requirements file to the working directory

.. code-block:: console

    RUN pip install --upgrade pip 
    COPY ./requirements.txt /usr/src/app
    RUN pip install -r requirements.txt

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

💡 Copy the current directory contents into the container at /usr/src/app

.. code-block:: console

    COPY . /usr/src/app

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

💡 Collect static files

.. code-block:: console

    RUN python manage.py collectstatic --noinput

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

💡 Command to run the application using Gunicorn

.. code-block:: console

    CMD gunicorn --bind 0.0.0.0:$PORT oc_lettings_site.wsgi

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

==========
Dockerfile
==========

⚙️ Dockerfile

.. code-block:: Dockerfile

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
    ENV SECRET_KEY=${SECRET_KEY}
    ENV DSN=${DSN}

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

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

==================
docker-compose.yml
==================


💡This docker-compose.yml file defines the services needed to run the application. 
It uses Docker Compose to manage Docker containers.

*   Services

    *   web: The "web" service is responsible for running the main application.

*   Configuration

    *   build: This option specifies that the Docker image for this service must be built using the Dockerfile located in the current directory.
    *   volumes: This service mounts the current directory to the ``/code`` directory inside the container, thus allowing to synchronize the code between the host and the container.
    *   ports: It maps port 8000 of the Docker container to port 8000 of the host, allowing access to the application via port 8000 of the host.


⚙️ ``docker-composer.yml``

.. code-block:: Dockerfile

    # This docker-compose.yml file defines the necessary services to run the application. 
    # It uses Docker Compose to manage Docker containers.
    version: '3.9'

    services:
    web:
        # Main service responsible for running the application.
        build: .
        # This option specifies that the Docker image for this service should be built using the
        # Dockerfile located in the current directory.
        volumes:
        - .:/code
        # This service mounts the current directory to the "/code" directory inside the container, 
        # allowing code synchronization between the host and the container.
        ports:
        - "8000:8000"
        # It maps port 8000 of the Docker container to port 8000 of the host, enabling access to 
        # the application via port 8000 of the host.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

***********
Build image
***********

⚙️ Perform this command to control the image

.. code-block:: Dockerfile

    Docker build -t orange_county_lettings .

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

************
Docker image
************

.. _ma_figure:

.. figure:: _static/docker_image.png
   :scale: 50
   :align: center
   :alt: docker image

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/docker_image.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

********************
Docker image details
********************

.. _ma_figure:

.. figure:: _static/docker_image_details.png
   :scale: 50
   :align: center
   :alt: docker image

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/docker_image_details.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------