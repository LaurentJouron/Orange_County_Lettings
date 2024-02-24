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

.. rubric:: CI (continuous integration) & CD (continuous deployment)

* Planning
* Compilation
* Integration
* Testing
* Measuring the quality
* Packaging / Management of application deliverables

.. _ma_figure:

.. figure:: _static/cicd.png
   :scale: 80
   :align: center
   :alt: CI/CD

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/cicd.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>


A pipeline in the context of continuous integration (CI) and continuous deployment (CD) is a 
series of automated steps that are executed in a specific order to test and deploy the code consistently 
and reliably.

.. _ma_figure:

.. figure:: _static/pepline_problem.png
   :scale: 40
   :align: center
   :alt: pepline_problem

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/pepline_problem.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*********
.circleci
*********

.. rubric:: Create a folder .circleci

We need to create a folder ``.circleci`` at the project level so that when the project is created, the ``config.py`` 
file is automatically placed inside it.

.. code-block:: console

        mkdir .circleci

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*********
config.py
*********

This file can be created and automatically positioned in the ``.cirlceci``. folder. 
A ``circleci-project-setup`` branch is created. Either you have to configure on this branch, 
or you have to gather it on the Master branch.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. _ma_figure:

.. figure:: _static/create_circle_ci.png
   :scale: 70
   :align: center
   :alt: create_circle_ci

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/create_circle_ci.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. _ma_figure:

.. figure:: _static/config_circle_file.png
   :scale: 80
   :align: center
   :alt: config_circle_file

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/config_circle_file.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. rubric:: config.py script

.. code-block:: python

        # Use the latest 2.1 version of CircleCI pipeline process engine.
        # See: https://circleci.com/docs/configuration-reference
        version: 2.1

        # Define a job to be invoked later in a workflow.
        # See: https://circleci.com/docs/jobs-steps/#jobs-overview & https://circleci.com/docs/configuration-reference/#jobs
        jobs:
        say-hello:
            # Specify the execution environment. You can specify an image from Docker Hub or use one of our convenience images from CircleCI's Developer Hub.
            # See: https://circleci.com/docs/executor-intro/ & https://circleci.com/docs/configuration-reference/#executor-job
            docker:
            # Specify the version you desire here
            # See: https://circleci.com/developer/images/image/cimg/base
            - image: cimg/base:current

            # Add steps to the job
            # See: https://circleci.com/docs/jobs-steps/#steps-overview & https://circleci.com/docs/configuration-reference/#steps
            steps:
            # Checkout the code as the first step.
            - checkout
            - run:
                name: "Say hello"
                command: "echo Hello, World!"

        # Orchestrate jobs using workflows
        # See: https://circleci.com/docs/workflows/ & https://circleci.com/docs/configuration-reference/#workflows
        workflows:
        say-hello-workflow: # This is the name of the workflow, feel free to change it to better match your workflow.
            # Inside the workflow, you define the jobs you want to run.
            jobs:
            - say-hello

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. rubric:: Merge branches

We must position ourselves on the marster branch.

.. code-block:: python

        git checkout master

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Then we can gather the branches, if necessary.

.. code-block:: python

        git merge circleci-project-setup

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. rubric:: config.py after configuration

.. code-block:: python

       # Use the latest 2.1 version of CircleCI pipeline process engine.
        # See: https://circleci.com/docs/configuration-reference
        version: 2.1

        orbs:

        python: circleci/python@2.1.1

        jobs:
        build_and_test:
        docker:
        - image: cimg/python:3.12.0

        steps:
        - checkout
        - python/install-packages:
                pkg-manager: pipenv
        - run:
                name: Run tests
                command:
                mkdir test-results && pipenv run pytest
        - store_test_results:
                path: test-results
        - store_artifacts:
                path: test-results
                destination: tr1
        - persist_to_workspace:
                root: ~/project
                paths:
                - .
        build-and-push-docker-image:
        docker:
        - image: cimg/python:3.9.6
        steps:
        - checkout
        - setup_remote_docker:
                docker_layer_caching: true
        - run:
                name: build and push docker image
                command: |
                TAG=0.1.$CIRCLE_BUILD_NUM
                docker build -t $DOCKER_USERNAME/$IMAGE_NAME:$TAG --build-arg SECRET_KEY=${SECRET_KEY} --build-arg DSN=${DSN} .
                #docker build -t $DOCKER_USERNAME/$IMAGE_NAME:$TAG .
                echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                docker push $DOCKER_USERNAME/$IMAGE_NAME:$TAG

        deploy_on_heroku:
        docker:
        - image: cimg/python:3.12.0

        steps:
        - checkout
        - setup_remote_docker:
                docker_layer_caching: true
        - run:
                name: Build and push Docker image to Heroku
                command: |
                sudo curl https://cli-assets.heroku.com/install.sh | sh
                HEROKU_API_KEY=${HEROKU_TOKEN} heroku config:set SECRET_KEY=$SECRET_KEY -a $HEROKU_APP_NAME
                HEROKU_API_KEY=${HEROKU_TOKEN} heroku config:set DSN=$DSN -a $HEROKU_APP_NAME
                HEROKU_API_KEY=${HEROKU_TOKEN} heroku container:login
                HEROKU_API_KEY=${HEROKU_TOKEN} heroku container:push -a $HEROKU_APP_NAME web
                HEROKU_API_KEY=${HEROKU_TOKEN} heroku container:release -a $HEROKU_APP_NAME web

        workflows:
        main:
        jobs:
        - build_and_test
        - build-and-push-docker-image:
                requires:
                - build_and_test
                filters:
                branches:
                only: main
        - deploy_on_heroku:
                requires:
                - build-and-push-docker-image
                filters:
                branches:
                only: main

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. raw:: html

   <a href="https://app.circleci.com/pipelines/github/LaurentJouron/Orange_County_Lettings" class="button">
       <img src="_static/button_all_pipelines.png" alt="Report button" width="200" height="100" />
   </a>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------