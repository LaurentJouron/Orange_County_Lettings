<h1 align="center">Bienvenue sur le readme de Orange County Lettings 👋</h1>
<p align="center">
  <a href="https://twitter.com/LaurentJouron">
    <img alt="Twitter: LaurentJouron" 
      src="https://img.shields.io/twitter/follow/LaurentJouron.svg?style=social" target="_blank" />
  </a>
  <a href="https://github.com/LaurentJouron">
    <img alt="GitHub followers" 
      src="https://img.shields.io/github/followers/LaurentJouron?style=social" />
  </a>
</p>

<p align="center">
    <img align="left"
      width="50px" 
      src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToscdusMNjQbffwasgiLuCsbCNZisJRE95Fg&usqp=CAU" />
</p>

### ``--- Explication en français ---``
_______________________

Cet exercice a été réalisé dans le cadre d'une formation 
_______________________

<h1 align="center">But de l'application</h1>

* Refonte de l'architecture modulaire dans le repository GitHub
* Réduction de diverses dettes techniques sur le projet
* Ajout d'un pipeline CI/CD ainsi que son déploiement
* Surveillance de l’application et suivi des erreurs via Sentry
* Création de la documentation technique de l’application avec Read The Docs et Sphinx.

_______________________

<h1 align="center">Langage et bibliothèques</h1>

<p align="center">L'intégralité de l'application a été développer en Python</p>


<table>
  <tr>
    <td align="center">
      <a href="https://www.python.org/">
        <img width="200px"
          src="https://www.python.org/static/img/python-logo.png" /><br />
        <sub><b>Téléchargez Python</b></sub></a><br />
      <a href="https://www.python.org/" title="Téléchargez Python" ></a> 
    </td>
</table>

_______________________

<h1 align="center">EDI</h1>


<p align="left">L'EDI utilisé pour la programmation est Visual Studio Code.

<table>
  <tr>
    <td align="center">
      <a href="https://visualstudio.microsoft.com/fr/">
        <img width="130px"
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-H3CcAG7w2nXSnlqldVWR-ER4mvFfLgqYxA&usqp=CAU" /><br />
        <sub><b>Visuable Studio Code</b></sub></a><br />
      <a href="https://visualstudio.microsoft.com/fr/" title="Visuable Studio Code" ></a>
    </td>
  </tr>
</table>

_______________________

<h1 align="center">Documentation </h1>

Pour vous rendre sur la documentation et voir toutes les fonctionnalités, [cliquer ici](https://laurent-lettings.readthedocs.io/en/latest/)
_______________________

<h1 align="center">Installation du site en local </h1>

Pour commencer il faut cloner le projet grâce à l'url suivante :
  * ``git clone https://github.com/LaurentJouron/Orange_County_Lettings.git``

Il faut se déplacer dans le dossier:
  * ``cd Orange_County_Lettings``

Voici la procédure pour afficher la page d'accueil du site:

Créer un répertoire avec le nom .venv
  * ``mkdir .venv``

Installer les bibliothèques nécessaires avec
  * ``pipenv install`` ou ``pip install``

Activer l'environnement de travail (environnement virtuel) avec
  * ``pipenv shell`` ou ``pip shell``

Lancez l'application avec cette commande
  * ``python manage.py runserver``

<a href="https://county-lettings-dce9820cf239.herokuapp.com/" title="Orange County Lettings" ></a>
<table>
  <tr>
    <td align="center">
      <a href="https://county-lettings-dce9820cf239.herokuapp.com/">
        <img width="200px"
          src="https://laurent-lettings.readthedocs.io/en/latest/_static/logo.png" /><br />
        <sub><b>Ouvrir le site</b></sub></a><br />
      <a href="https://county-lettings-dce9820cf239.herokuapp.com/" title="Ouvrir le site" ></a> 
    </td>
</table>

_______________________

<h1 align="center">Admin</h1>

* Pour se rendre sur l'administration du site en local [cliquer ici (uniquement après installation)](http://localhost:8000/admin)

* Pour se rendre sur l'administration du site déployé [cliquer ici](https://county-lettings-dce9820cf239.herokuapp.com/admin/login/?next=/admin/)

<h3>Compte et mot de passe</h3>

* Compte utilisateur `admin`
* Mot de passe `Abc1234!`

_______________________

<h1 align="center">Flake8</h1>

<a href="https://flake8.pycqa.org/" title="Ouvrir la documentation" ></a>
<table>
  <tr>
    <td align="center">
      <a href="https://flake8.pycqa.org/">
        <img width="200px"
          src="https://img.shields.io/badge/flake8-%234B8BBE.svg?style=for-the-badge&logo=flake8&logoColor=white" /><br />
        <sub><b>Ouvrir la documentation</b></sub></a><br />
      <a href="https://flake8.pycqa.org/" title="Ouvrir la documentation" ></a> 
    </td>
</table>

<p>Flake8 est un outil d’analyse de code statique en Python. Il vérifie si votre code suit les conventions de style définies dans PEP 8, qui est le guide de style officiel pour le code Python. En plus de vérifier le style, Flake8 peut également détecter des erreurs potentielles dans le code en utilisant des plugins pour examiner la qualité du code et identifier les problèmes logiques. En résumé, Flake8 aide à maintenir un code Python propre, lisible et sans erreur.
</p>

Activer falke8 avec cette commande en étant à la racine du projet

  * ``flake8``

_______________________

<h1 align="center">Pytest</h1>

<a href="https://pytest-django.readthedocs.io/en/latest/" title="Ouvrir la documentation" ></a>
<table>
  <tr>
    <td align="center">
      <a href="https://pytest-django.readthedocs.io/en/latest/">
        <img width="200px"
          src="https://img.shields.io/badge/pytest--django-%232C8736.svg?style=for-the-badge&logo=pytest&logoColor=white" /><br />
        <sub><b>Ouvrir la documentation</b></sub></a><br />
      <a href="https://pytest-django.readthedocs.io/en/latest/" title="Ouvrir la documentation" ></a> 
    </td>
</table>

Pour vous rendre sur la documentation orange county lettings et voir tous les tests, [cliquer ici](https://laurent-lettings.readthedocs.io/en/latest/test.html)

_______________________

<h1 align="center">CircleCI</h1>

<a href="https://circleci.com/docs/" title="Ouvrir la documentation" ></a>
<table>
  <tr>
    <td align="center">
      <a href="https://circleci.com/docs/">
        <img width="200px"
          src="https://img.shields.io/badge/circle%20ci-%23161616.svg?style=for-the-badge&logo=circleci&logoColor=white" /><br />
        <sub><b>Ouvrir la documentation</b></sub></a><br />
      <a href="https://circleci.com/docs/" title="Ouvrir la documentation" ></a> 
    </td>
</table>

Pour vous rendre sur la documentation orange county lettings et voir tous les pipelines, [cliquer ici](https://app.circleci.com/pipelines/github/LaurentJouron/Orange_County_Lettings)

_______________________

<h1 align="center">Sentry</h1>

<a href="https://docs.sentry.io/" title="Ouvrir la documentation" ></a>
<table>
  <tr>
    <td align="center">
      <a href="https://docs.sentry.io/">
        <img width="200px"
          src="https://img.shields.io/badge/sentry-%2319CAAD.svg?style=for-the-badge&logo=sentry&logoColor=white" /><br />
        <sub><b>Ouvrir la documentation</b></sub></a><br />
      <a href="https://docs.sentry.io/" title="Ouvrir la documentation" ></a> 
    </td>
</table>

Pour vous rendre sur la documentation orange county lettings et voir tous les rapports de gestion des erreurs, [cliquer ici](https://ace-xk.sentry.io/performance/?project=4506710341844992)
_______________________

<h1 align="center">Sphinx</h1>

<a href="https://www.sphinx-doc.org/" title="Ouvrir la documentation" ></a>
<table>
  <tr>
    <td align="center">
      <a href="https://www.sphinx-doc.org/">
        <img width="200px"
          src="https://img.shields.io/badge/sphinx-%23C4302B.svg?style=for-the-badge&logo=sphinx&logoColor=white" /><br />
        <sub><b>Ouvrir la documentation</b></sub></a><br />
      <a href="https://www.sphinx-doc.org/" title="Ouvrir la documentation" ></a> 
    </td>
</table>

Pour se rendre sur la documentation du site Orange County Lettings [cliquer ici](https://laurent-lettings.readthedocs.io/en/latest/)

_______________________


<h1 align="center">Auteur et collaborateurs</h1>

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/LaurentJouron">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlW-w7O7g3hQTw8qcIAy3LCRhiHg5tUPfvVg&usqp=CAU"
          width="100px;"/><br />
        <sub><b>Laurent Jouron</b></sub></a><br />
      <a href="https://openclassrooms.com/fr/" title="Étudiant">🈸</a>
      <a href="https://github.com/LaurentJouron/Books-online" title="Codeur de l'application">💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/thierhost">
        <img src="https://avatars.githubusercontent.com/u/7854284?s=100&v=4"
          width="100px;"/><br />
        <sub><b>Thierno Thiam</b></sub></a><br />
      <a href="https://github.com/thierhost" title="Mentor de Laurent">👨‍🏫</a> 
      <a href="https://www.python.org/dev/peps/pep-0008/" title="Doc PEP 8">📄</a>
    </td>
  </tr>
</table>
