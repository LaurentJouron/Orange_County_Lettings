.. _circleci:

**Circle CI**
============

CircleCI is a continuous integration and continuous deployment (CI/CD) tool widely used in software development.
Pipelines in CircleCI are automated workflows that describe how code is compiled, tested, and deployed.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*************
Pipline CI/CD
*************

A pipeline in the context of continuous integration (CI) and continuous deployment (CD) is a 
series of automated steps that are executed in a specific order to test and deploy the code consistently 
and reliably.

.. code-block:: python

        version: 2.1

        jobs:
        build:
            docker:
            - image: python:3.12
            steps:
            - checkout
            - run: pip install -r requirements.txt
            - run: python manage.py migrate
            - run: python manage.py test

        workflows:
        version: 2
        build_and_deploy:
            jobs:
            - build

* We define a job named "build" that uses a Docker Python 3.12 image.
* Steps in this job include retrieving source code, installing dependencies, running database migrations, and running tests.
* Then we define a workflow named "build_and_deploy" which simply includes the "build" job.


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*******
Project
*******

Créer un fichier de configuration : CircleCI utilise un fichier de configuration YAML (généralement nommé .circleci/config.yml) pour définir votre pipeline. Ce fichier contient les étapes à exécuter, ainsi que les dépendances et les paramètres nécessaires.

Configurer les déclencheurs : Déterminez les événements qui doivent déclencher l'exécution de votre pipeline. Cela peut inclure des commits sur certaines branches de votre dépôt Git, des demandes de fusion (pull requests), ou des déclencheurs planifiés.

Configurer les jobs : Définissez les différentes tâches à exécuter dans votre pipeline en tant que jobs. Chaque job représente une étape de votre pipeline, comme la compilation, les tests unitaires, les tests d'intégration, etc.

Configurer les workflows : Les workflows permettent de définir l'ordre dans lequel les jobs doivent être exécutés et les conditions sous lesquelles ils doivent l'être. Vous pouvez définir des workflows pour gérer différentes branches de votre dépôt, des événements spécifiques, ou des conditions personnalisées.

Tester la configuration : Avant de déployer votre pipeline en production, assurez-vous de la tester localement ou sur des environnements de développement pour vous assurer qu'elle fonctionne comme prévu.

Déployer la configuration : Une fois que vous êtes satisfait de votre configuration, déployez-la sur votre compte CircleCI et associez-la à votre dépôt Git.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****************
readthedocs
*****************


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*******
conf.py
*******

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

****************
requirements.txt
****************


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****************
Schema of the doc
*****************

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


