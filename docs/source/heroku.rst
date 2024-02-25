.. _heroku:

**Heroku**
==========


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

https://county-lettings-dce9820cf239.herokuapp.com/

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****************

*****************

.. warning:: Before activating the button below, you must install and activate the virtual environment.

⏩️
⏩️ 

.. raw:: html

   <a href="https://county-lettings-dce9820cf239.herokuapp.com/" class="button">
       <img src="_static/button_open_website.png" alt="Report button" width="200" height="100" />
   </a>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


.. tabs::

   .. tab:: Sphinx

      We recommend the `sphinx-notfound-page`_ extension,
      which Read the Docs maintains.
      It automatically creates a ``404.html`` page for your documentation,
      matching the theme of your project.
      See its documentation_ for how to install and customize it.

      If you want to create a custom ``404.html``,
      Sphinx uses `html_extra_path`_ option to add static files to the output.
      You need to create a ``404.html`` file and put it under the path defined in ``html_extra_path``.

      If you are using the ``DirHTML`` builder,
      no further steps are required.
      Sphinx will automatically apply the ``<page-name>/index.html`` folder structure to your 404 page:
      ``404/index.html``.
      Read the Docs also detects 404 pages named this way.

   .. tab:: MkDocs

      MkDocs automatically generates a ``404.html`` which Read the Docs will use.
      However, assets will not be loaded correctly unless you define the `site_url`_ configuration value as your site's
      :ref:`canonical base URL <guides/canonical-urls:MkDocs>`.

      