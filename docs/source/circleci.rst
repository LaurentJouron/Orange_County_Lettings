.. _circleci:

**Circle CI**
============

.. important::

    .. image:: https://img.shields.io/badge/circle%20ci-%23161616.svg?style=for-the-badge&logo=circleci&logoColor=white
        :alt: CircleCi Badge
        :target: https://circleci.com/docs/

    Parameterizations are done to a specific project. To parameterize to the other project, go to the official 
    documentation.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

****************
What is CircleCi
****************

CircleCI is a continuous integration and continuous deployment (CI/CD) 
tool widely used in software development.
Pipelines in CircleCI are automated workflows that describe how code is compiled, tested, and deployed.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*************
Pipline CI/CD
*************

A pipeline in the context of continuous integration (CI) and continuous deployment (CD) is a 
series of automated steps that are executed in a specific order to test and deploy the code consistently 
and reliably.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*******
conf.py
*******

.. rubric:: Create a folder .circleci

.. code-block:: console
    
        mkdir .circleci

.. rubric:: Place in it

.. code-block:: console
    
        cd .circleci


.. rubric:: Create a file conf.py for Unix/Linux/macOS 

.. code-block:: console

        touch conf.py


.. rubric:: Create a file conf.py for Windows

.. code-block:: console

        echo "version: 2.1" > conf.py


.. rubric:: conf.py script
 
.. code-block:: python

        version: 2.1

        orbs:
        python: circleci/python@2.1.1

        jobs:
        build_and_test: build and test
            docker:
            - image: cimg/python:3.12.0

            steps:
            - checkout
            - python/install-packages:
                pkg-manager: pipenv
                pip-dependency-file: requirements.txt
            - run:
                name: check test with Pytest
                command: pytest --nomigrations --disable-warnings

        flake8:
            docker:
            - image: cimg/python:3.12.0
            steps:
            - checkout
            - run:
                name: Install Flake8
                command: pip install flake8==3.7.0
            - run:
                name: check linting with Flake8
                command: flake8

        build-push-docker:
            docker:
            - image: cimg/python:3.12.0
            steps:
            - checkout
            - setup_remote_docker
            - run:
                name: Build docker image
                command:
                    docker build -t $DOCKER_IMAGE:latest .
            - run:
                name: Connect to Docker Hub
                command:
                    echo "$DOCKER_HUB_PASSWORD" | docker login -u "$DOCKER_HUB_USER_ID" --password-stdin
            - run:
                name: Push docker image
                command:
                    docker tag $DOCKER_IMAGE $DOCKER_IMAGE |
                    docker push $DOCKER_IMAGE

        deploy-from-dockerhub-to-render:
            docker:
            - image: curlimages/curl:latest
            steps:
            - run:
                name: Deploy docker hub image to Render
                command: curl $DEPLOY_HOOK

        workflows:
        run_tests_and_build_docker:
            jobs:
            - flake8
            - build-push-docker:
                filters:
                    branches:
                    only: master
                requires:
                    - flake8
            - deploy-from-dockerhub-to-render:
                filters:
                    branches:
                    only: master
                requires:
                    - build-push-docker

* We define a job named "build" that uses a Docker Python 3.12 image.
* Steps in this job include retrieving source code, installing dependencies, running database migrations, and running tests.
* Then we define a workflow named "build_and_deploy" which simply includes the "build" job.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*******

*******


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****************

*****************


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

****************

****************


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****************

*****************

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------