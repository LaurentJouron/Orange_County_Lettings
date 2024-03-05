.. _documentation:

**Documentation**
=================

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

********
Creation
********

.. important::

    .. image:: https://img.shields.io/badge/sphinx-%23C4302B.svg?style=for-the-badge&logo=sphinx&logoColor=white
        :alt: Sphinx Badge
        :target: https://www.sphinx-doc.org/en/master/index.html
    
    **After creating the project** and activating the virtual environment, you can start.
    To start create documentation, you must install `Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_ 
    

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⏩️ Install Sphinx

.. code-block:: console

   pipenv install sphinx

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚙️ Creating the documentation layout (``docs``)

.. code-block:: console

   sphinx-quickstart docs

This will present to you a series of questions required to create the basic directory and configuration layout for your 
project inside the docs folder. To proceed, answer each question as follows:

* Separate source and build directories (y/n) [n]: y

* Project name: Orange County Lettings

* Author name: Laurent Jouron

* Project release []: 0.1

* Project language [en]: Leave it empty (the default, English) and press Enter.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*******
Project
*******

After the last question, you will see the new docs directory with the following content.

.. figure:: _static/doc_project.png
   :scale: 75
   :align: center
   :alt: doc project

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The purpose of each of these files is:

💡build/

* An empty directory (for now) that will hold the rendered documentation.

💡make.bat and Makefile

* Convenience scripts to simplify some common Sphinx operations, such as rendering the content.

💡source/conf.py

* A Python script holding the configuration of the Sphinx project. It contains the project name and release you specified to sphinx-quickstart, as well as some extra configuration keys.

💡source/index.rst

* The root document of the project, which serves as welcome page and contains the root of the “table of contents tree” (or toctree).

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚙️ Build docs/build/

Thanks to this bootstrapping step, you already have everything needed to render the documentation as HTML for the first time. 
To do that, run this command:

.. code-block:: console

   sphinx-build -M html docs/source/ docs/build/

And finally, open docs/build/html/index.html in your browser. You should see something like this:

.. figure:: _static/doc_view.png
   :scale: 75
   :align: center
   :alt: Logo

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⏩️ Position yourself in the docs folder

.. code-block:: console

   cd docs

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚙️ make html

This command must be retained because this command will be repeated with each modification.

.. code-block:: console

   .\make html

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****************
.readthedocs.yaml
*****************

To realize this documentation I used this configuration for the file ``.readthedocs.yaml``

⚙️ .readthedocs.yaml

.. code-block:: python

    # Required
    version: 2

    # Set the OS, Python version and other tools you might need
    build:
    os: ubuntu-22.04
    tools:
        python: "3.12"

    # Build documentation in the "docs/" directory with Sphinx
    sphinx:
    configuration: docs/source/conf.py

    python:
    install:
        - requirements: docs/requirements.txt

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*******
conf.py
*******

To realize this documentation I used this configuration for the file ``conf.py``

⚙️ ``conf.py``

.. code-block:: python

    # Configuration file for the Sphinx documentation builder.
    #
    # For the full list of built-in configuration values, see the documentation:
    # https://www.sphinx-doc.org/en/master/usage/configuration.html

    # -- Project information -----------------------------------------------------
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

    project = "Orange County Lettings"
    copyright = "2024, Laurent Jouron"
    author = "Laurent Jouron"
    release = "1.0.0"

    # -- General configuration ---------------------------------------------------
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

    extensions = [
        "sphinx_copybutton",
        "sphinx.ext.duration",
        "sphinx.ext.autodoc",
        "sphinx.ext.doctest",
        "sphinx.ext.intersphinx",
        "sphinx.ext.todo",
    ]

    autodoc_default_flags = []

    autodoc_modules = {
        "lettings": "lettings",
        "profiles": "profiles",
        "oc_lettings_site": "oc_lettings_site",
    }

    # The suffix of source filenames.
    source_suffix = {
        ".rst": "restructuredtext",
        ".txt": "restructuredtext",
        ".md": "markdown",
    }

    # The master toctree document.
    master_doc = "index"

    templates_path = ["_templates"]
    exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

    # The name of the Pygments (syntax highlighting) style to use.
    pygments_style = "sphinx"
    epub_show_urls = "footnote"


    # -- Options for HTML output -------------------------------------------------
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

    html_theme_options = {
        "display_version": False,
        "style_external_links": True,
    }

    html_theme = "sphinx_rtd_theme"
    html_logo = "_static/logo.png"
    html_static_path = ["_static"]

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

****************
requirements.txt
****************

To realize this documentation I used this configuration for the file ``requirements.txt``

⚙️ requirements.txt

.. code-block:: Python

    Sphinx==7.2.6
    sphinx-rtd-theme==1.3.0
    sphinx-bootstrap-theme
    sphinx-copybutton

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****************
Schema of the doc
*****************

Circle CI
~~~~~~~~~

* :doc:`Circle CI <circleci>`

  - `What is Circle CI <http://127.0.0.1:5501/docs/build/html/circleci.html#what-is-circleci>`_
  - `Pipeline CI/CD <http://127.0.0.1:5501/docs/build/html/circleci.html#pipline-ci-cd>`_
  - `.circleci <http://127.0.0.1:5501/docs/build/html/circleci.html#id2>`_
  - `config.py <http://127.0.0.1:5501/docs/build/html/circleci.html#config-py>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Data structure
~~~~~~~~~~~~~~

* :doc:`Data structure <data_structure>`

  - `Admin start structure <http://127.0.0.1:5501/docs/build/html/data_structure.html#admin-start-structure>`_
  - `Project table <http://127.0.0.1:5501/docs/build/html/data_structure.html#project-table>`_
  - `Address <http://127.0.0.1:5500/docs/build/html/data_structure.html#address>`_
  - `Lettings <http://127.0.0.1:5500/docs/build/html/data_structure.html#lettings>`_
  - `Profiles <http://127.0.0.1:5500/docs/build/html/data_structure.html#profile>`_
  - `Schema <http://127.0.0.1:5500/docs/build/html/data_structure.html#schema>`_
  - `Admin end structure <http://127.0.0.1:5501/docs/build/html/data_structure.html#admin-end-structure>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Description
~~~~~~~~~~~

* :doc:`Description <description>`

  - `Start <http://127.0.0.1:5500/docs/build/html/description.html#start>`_
  - `Prerequiste <http://127.0.0.1:5500/docs/build/html/description.html#prerequisite>`_
  - `To do <http://127.0.0.1:5500/docs/build/html/description.html#to-do>`_
  - `Final description <http://127.0.0.1:5500/docs/build/html/description.html#final-description>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Docker
~~~~~~

* :doc:`Docker <docker>`

  - `Dockerfile for Python <http://127.0.0.1:5501/docs/build/html/docker.html#dockerfile-for-python>`_
  - `Dockerfile <http://127.0.0.1:5501/docs/build/html/docker.html#dockerfile>`_
  - `docker-compose.yml <http://127.0.0.1:5501/docs/build/html/docker.html#docker-compose-yml>`_

      - `Build image <http://127.0.0.1:5501/docs/build/html/docker.html#build-image>`_
      - `Docker image <http://127.0.0.1:5501/docs/build/html/docker.html#docker-image>`_
      - `Docker image details <http://127.0.0.1:5501/docs/build/html/docker.html#docker-image-details>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Docstring
~~~~~~~~~

* :doc:`Docstring <docstring>`

  - `What the docstrings <http://127.0.0.1:5501/docs/build/html/docstring.html#what-the-docstrings>`_
  - `Google style <http://127.0.0.1:5501/docs/build/html/docstring.html#google-style>`_
  - `NumPy/Scipy style <http://127.0.0.1:5501/docs/build/html/docstring.html#numpy-scipy-style>`_
  - `Display docstrings <http://127.0.0.1:5501/docs/build/html/docstring.html#display-docstrings>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Documentation
~~~~~~~~~~~~~

* :doc:`Documentation <documentation>`

  - `Creation <http://127.0.0.1:5500/docs/build/html/documentation.html#creation>`_
  - `Project <http://127.0.0.1:5500/docs/build/html/documentation.html#project>`_
  - `.readthedocs.yaml <http://127.0.0.1:5500/docs/build/html/documentation.html#readthedocs-yaml>`_
  - `conf.py <http://127.0.0.1:5500/docs/build/html/documentation.html#conf-py>`_
  - `requirements.txt <http://127.0.0.1:5500/docs/build/html/documentation.html#requirements-txt>`_
  - `Schema of the doc <http://127.0.0.1:5500/docs/build/html/documentation.html#schema-of-the-doc>`_

      - `Circle CI <http://127.0.0.1:5501/docs/build/html/documentation.html#circle-ci>`_
      - `Data structure <http://127.0.0.1:5501/docs/build/html/documentation.html#data-structure>`_
      - `Description <http://127.0.0.1:5501/docs/build/html/documentation.html#description>`_
      - `Docker <http://127.0.0.1:5501/docs/build/html/documentation.html#docker>`_
      - `Docstring <http://127.0.0.1:5501/docs/build/html/documentation.html#docstring>`_
      - `Documentation <http://127.0.0.1:5501/docs/build/html/documentation.html#id7>`_
      - `Error <http://127.0.0.1:5501/docs/build/html/documentation.html#error>`_
      - `Flake8 <http://127.0.0.1:5501/docs/build/html/documentation.html#flake8>`_
      - `Heroku <http://127.0.0.1:5501/docs/build/html/documentation.html#heroku>`_
      - `Pipelines <http://127.0.0.1:5501/docs/build/html/documentation.html#pipelines>`_
      - `Quick start <http://127.0.0.1:5501/docs/build/html/documentation.html#quick-start>`_
      - `Sentry <http://127.0.0.1:5501/docs/build/html/documentation.html#sentry>`_
      - `Pytest Django <http://127.0.0.1:5501/docs/build/html/documentation.html#pytest-django>`_
      - `Web site <http://127.0.0.1:5501/docs/build/html/documentation.html#web-site>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Error
~~~~~

* :doc:`Error <error>`

  - `404 Error <http://127.0.0.1:5501/docs/build/html/error.html#id2>`_
  - `500 Error <http://127.0.0.1:5501/docs/build/html/error.html#id3>`_
  - `Summary <http://127.0.0.1:5501/docs/build/html/error.html#summary>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Flake8
~~~~~~

* :doc:`Flake8 <flake8>`

  - `What is Flake8 <http://127.0.0.1:5501/docs/build/html/flake8.html#what-is-flake8>`_
  - `Install Flake8 <http://127.0.0.1:5501/docs/build/html/flake8.html#install-flake8>`_
  - `.flake8 <http://127.0.0.1:5501/docs/build/html/flake8.html#id2>`_
  - `Using Flake8 <http://127.0.0.1:5501/docs/build/html/flake8.html#using-flake8>`_
  - `What is Flake8-html <http://127.0.0.1:5501/docs/build/html/flake8.html#what-is-flake8-html>`_
  - `Install Flake8-html <http://127.0.0.1:5501/docs/build/html/flake8.html#install-flake8-html>`_
  - `Flake8 pipelines <http://127.0.0.1:5501/docs/build/html/flake8.html#flake8-pipelines>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Heroku
~~~~~~

* :doc:`Heroku <heroku>`

  - `Heroku and CLI <http://127.0.0.1:5501/docs/build/html/heroku.html#heroku-and-cli>`_
  - `Signup <http://127.0.0.1:5501/docs/build/html/heroku.html#signup>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Pipelines
~~~~~~~~~

* :doc:`Pipelines <pipeline>`

  - `Spin up environment <http://127.0.0.1:5501/docs/build/html/pipeline.html#spin-up-environment>`_
  - `Preparing environment variables <http://127.0.0.1:5501/docs/build/html/pipeline.html#preparing-environment-variables>`_
  - `Checkout code <http://127.0.0.1:5501/docs/build/html/pipeline.html#checkout-code>`_
  - `Link lockfile <http://127.0.0.1:5501/docs/build/html/pipeline.html#link-lockfile>`_
  - `Save Python version <http://127.0.0.1:5501/docs/build/html/pipeline.html#save-python-version>`_
  - `Restoring cache <http://127.0.0.1:5501/docs/build/html/pipeline.html#restoring-cache>`_
  - `Move restored cache <http://127.0.0.1:5501/docs/build/html/pipeline.html#move-restored-cache>`_
  - `Install dependencies with pipenv <http://127.0.0.1:5501/docs/build/html/pipeline.html#install-dependencies-with-pipenv-using-project-pipfile-or-inline-packages>`_
  - `Saving cache <http://127.0.0.1:5501/docs/build/html/pipeline.html#saving-cache>`_
  - `Run test <http://127.0.0.1:5501/docs/build/html/pipeline.html#run-test>`_
  - `Persisting to workspace <http://127.0.0.1:5501/docs/build/html/pipeline.html#persisting-to-workspace>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Quick start
~~~~~~~~~~~

* :doc:`Quick start <quick_start>`

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sentry
~~~~~~

* :doc:`Sentry <sentry>`

  - `What is Sentry <http://127.0.0.1:5501/docs/build/html/sentry.html#what-is-sentry>`_
  - `Install Sentry <http://127.0.0.1:5501/docs/build/html/sentry.html#install-sentry>`_
  - `.env <http://127.0.0.1:5501/docs/build/html/sentry.html#env>`_
  - `settings.py <http://127.0.0.1:5501/docs/build/html/sentry.html#settings-py>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Pytest-Django
~~~~~~~~~~~~~

* :doc:`Pytest-Django <test>`

  - `Configuration <http://127.0.0.1:5501/docs/build/html/test.html#configuration>`_
  - `pytest.ini <http://127.0.0.1:5501/docs/build/html/test.html#pytest-ini>`_
  - `Run test <http://127.0.0.1:5501/docs/build/html/test.html#run-test>`_
  - `pytest -vvv <http://127.0.0.1:5501/docs/build/html/test.html#pytest-vvv>`_
  - `pytest -cov=. <http://127.0.0.1:5501/docs/build/html/test.html#pytest-cov>`_
  - `Report HTML <http://127.0.0.1:5501/docs/build/html/test.html#report-html>`_
  - `Report pipelines test <http://127.0.0.1:5501/docs/build/html/test.html#report-html>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Web site
~~~~~~~~

* :doc:`Web site <website>`

  - `Reception <http://127.0.0.1:5501/docs/build/html/website.html>`_
  - `Middle button <http://127.0.0.1:5501/docs/build/html/website.html#middle-button>`_
  - `Down button <http://127.0.0.1:5501/docs/build/html/website.html#down-button>`_
  - `Lettings <http://127.0.0.1:5501/docs/build/html/website.html#lettings>`_
  - `profiles <http://127.0.0.1:5501/docs/build/html/website.html#profiles>`_
