.. _docker:

Docker
======

.. important::

    .. image:: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
        :alt: Docker Badge
        :target: https://www.sqlite.org/index.html

    Parameterizations are done to a specific project. To parameterize to the other project, go to the official 
    documentation `Docker <https://docs.docker.com/>`_.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****************
What is container
*****************

A container is an isolated environment that includes:

    * Own processes
    * Its own dependencies/ libraries/ binaries.
    * Its own file tree.
    * Its own network interfaces and ports.

A container can be started, duplicated, paused, stopped.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**********
Why Docker
**********

**Insulation**
    * A container has its own environment, its own dependency versions/ libraries/ binaries.

**Deployment**
    * Starting an application on a new machine is very Fast, the application is pre-packaged with what it needs.

**Performance**
    * Containerization is very efficient in terms of use resourceful.

**Portability**
    * The app can be deployed on multiple types of transparently.

**Scalability**
    * A container can be easily duplicated to create a horizontal scalability.

**Safety**
    * Containers and processes are isolated from the rest of the system.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**********
Docker Hub
**********

To launch a container, we need an **image**.

`Docker Hub <https://hub.docker.com/>`_ is the main registry of Docker, it contains many images basic (servers, bones, tools, databases, applications...).

`Docker Hub <https://hub.docker.com/>`_ allows you to search for images and see tags available for this image.

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

**FROM**
    * Set the source image

**RUN**
    * Run commands in a container

**ADD**
    * Add files to a container

**WORKDIR**
    * Used to define the working directory

**EXPOSE**
    * Set default listening ports

**VOLUME**
    * Defines usable volumes

**CMD**
    * Set the default command when running your Docker containers.


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

***********
Build image
***********

⚙️ Perform this command to control the image

.. code-block:: Dockerfile

    docker build -t orange_county_lettings .

.. rubric:: ⏩️ Launch Docker project

Launch the container in detached mode on a specific port (8000 for example).

.. code-block:: Dockerfile

    docker run -d -p 8000:8000 orange_county_lettings

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

***************
Docker commands
***************

Commands that `list all images <https://docs.docker.com/trusted-content/official-images/>`_:

.. code-block:: Dockerfile

    docker images

.. figure:: _static/docker_no_image_console.png
   :scale: 80
   :align: center
   :alt: docker no console image

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/docker_no_image_console.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Commands that `list the containers <https://docs.docker.com/reference/cli/docker/stack/ps/>`_ available on the computer:

.. code-block:: Dockerfile

    docker ps

.. figure:: _static/docker_no_container_console.png
   :scale: 80
   :align: center
   :alt: docker no container console

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/docker_no_container_console.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To use this image, download it on `Docker Hub <https://hub.docker.com/r/jouron/orange_county_lettings>`_.

.. code-block:: Dockerfile

    docker pull jouron/orange_county_lettings

.. figure:: _static/docker_pull_image.png
   :scale: 70
   :align: center
   :alt: docker no container console

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/docker_pull_image.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you relaunch the `first command <https://docs.docker.com/trusted-content/official-images/>`_ we made, we see the list of images:

.. code-block:: Dockerfile

    docker images

.. figure:: _static/docker_image_console.png
   :scale: 80
   :align: center
   :alt: docker console image

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/docker_image_console.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

controls to run the image in interactive mode. The local run container.

.. code-block:: Dockerfile

    docker run -it jouron/orange_county_lettings

.. figure:: _static/docker_run_it_container.png
   :scale: 60
   :align: center
   :alt: docker run intervative container

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/docker_run_it_container.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Commands that `list the containers <https://docs.docker.com/reference/cli/docker/stack/ps/>`_ available on the computer

.. code-block:: Dockerfile

    docker ps

.. figure:: _static/docker_list_container.png
   :scale: 60
   :align: center
   :alt: docker container console

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/docker_list_container.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Commands to `stop a container <https://docs.docker.com/reference/cli/docker/container/stop/>`_ by adding the ID of it.

.. code-block:: Dockerfile

    docker stop  "ID"

.. figure:: _static/docker_stop_container.png
   :scale: 60
   :align: center
   :alt: docker container console

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/docker_stop_container.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Controls to rotate the container in detached (in the background).

.. code-block:: Dockerfile

    docker run -it -d jouron/orange_county_lettings

.. figure:: _static/docker_run_it_detached.png
   :scale: 70
   :align: center
   :alt: docker run container it detached console

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/docker_run_it_detached.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. code-block:: Dockerfile

    docker ps

If you re-run the command to `see the containers <https://docs.docker.com/reference/cli/docker/stack/ps/>`_ that are running, we see the list of containers.


.. figure:: _static/docker_run_container_it_d.png
   :scale: 60
   :align: center
   :alt: docker run container detached console

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/docker_run_container_it_d.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Commands to `stop a container <https://docs.docker.com/reference/cli/docker/container/stop/>`_ by adding the ID of it.

.. code-block:: Dockerfile

    docker stop  "ID"

List container:

.. code-block:: Dockerfile

    docker ps

.. figure:: _static/docker_stop_container.png
   :scale: 60
   :align: center
   :alt: docker stop container console

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/docker_stop_container.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

System `cleaning <https://docs.docker.com/reference/cli/docker/volume/prune/>`_ controls.

.. code-block:: Dockerfile

    docker system prune

.. figure:: _static/docker_system_prune.png
   :scale: 60
   :align: center
   :alt: docker cleaning container

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/docker_system_prune.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Command to `delete images <https://docs.docker.com/reference/cli/docker/volume/prune/>`_ (caution suppresion without possibility of return).

.. code-block:: Dockerfile

    docker system prune -a

.. figure:: _static/docker_system_prune_a.png
   :scale: 60
   :align: center
   :alt: docker cleaning container -a

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/docker_system_prune_a.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Link our previously created **orange_county_lettings:latest** image to the Docker Hub **jouron/orange_county_lettings:latest**

.. code-block:: Dockerfile

    docker tag orange_county_lettings:latest jouron/orange_county_lettings:latest

Run a final command to send the image to the Docker Hub.

.. code-block:: Dockerfile

    docker push jouron/orange_county_lettings:latest

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

********************
Docker image details
********************

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

**************
Quit container
**************

.. rubric:: 🔚 Quit

To stop the server, press

.. code-block:: console

   ctrl + c

(SIGNIT signal)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**************
Deployed image
**************

.. figure:: _static/docker_image_deploye.png
   :scale: 50
   :align: center
   :alt: docker image deploye on Docker hub

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/docker_image_deploye.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. raw:: html

   <a href="https://hub.docker.com/repository/docker/jouron/orange_county_lettings/general" class="button" target=_blank>
       <img src="_static/button_docker_hub.png" alt="Report button" width="200" height="100" />
   </a>

