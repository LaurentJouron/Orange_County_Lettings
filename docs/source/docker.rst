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

********
Terminal
********


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*******

*******


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****************

*****************


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*******

*******

docker build -t orange_county_lettings .

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

****************

****************
Assurez-vous d'avoir un compte Heroku et l'interface de ligne de commande Heroku (CLI) installée sur votre machine locale.

Connectez-vous à votre compte Heroku en utilisant la commande suivante dans votre terminal :

heroku login

Une fois connecté, créez une nouvelle application Heroku en exécutant la commande suivante :
heroku create orange_county_lettings

Ensuite, vous devez pousser votre image Docker vers le registre d'images de conteneurs Heroku en utilisant la commande suivante :
heroku container:push web --app orange_county_lettings

Après avoir poussé votre image Docker vers Heroku, vous devez libérer cette image en exécutant la commande suivante :
heroku container:release web --app orange_county_lettings

Enfin, pour vous assurer que votre application est en cours d'exécution, vous pouvez utiliser la commande suivante pour afficher les journaux en temps réel :
heroku logs --tail --app nom_de_votre_application


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****************

*****************

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


