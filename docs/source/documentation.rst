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

💡 build/

* An empty directory (for now) that will hold the rendered documentation.

💡 make.bat and Makefile

* Convenience scripts to simplify some common Sphinx operations, such as rendering the content.

💡 source/conf.py

* A Python script holding the configuration of the Sphinx project. It contains the project name and release 
you specified to sphinx-quickstart, as well as some extra configuration keys.

💡 source/index.rst

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

.. code-block:: txt

    Sphinx==7.2.6
    sphinx-rtd-theme==1.3.0
    sphinx-bootstrap-theme
    sphinx-copybutton
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****************
Schema of the doc
*****************

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Circle CI
~~~~~~~~~

* `Circle CI <http://127.0.0.1:5501/docs/build/html/circleci.html>`_

  - `What is Circle CI <http://127.0.0.1:5501/docs/build/html/circleci.html#what-is-circleci>`_

  - `Pipeline CI/CD <http://127.0.0.1:5501/docs/build/html/circleci.html#pipline-ci-cd>`_

  - `.circleci <http://127.0.0.1:5501/docs/build/html/circleci.html#id2>`_

  - `config.py <http://127.0.0.1:5501/docs/build/html/circleci.html#config-py>`_
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Data structure
~~~~~~~~~~~~~~

* `Data structure <http://127.0.0.1:5500/docs/build/html/data_structure.html>`_

  - `Specifications <http://127.0.0.1:5500/docs/build/html/data_structure.html#need-for-the-specifications>`_

  - `Address <http://127.0.0.1:5500/docs/build/html/data_structure.html#address>`_

  - `Lettings <http://127.0.0.1:5500/docs/build/html/data_structure.html#lettings>`_

  - `Profile <http://127.0.0.1:5500/docs/build/html/data_structure.html#profile>`_

  - `Schema <http://127.0.0.1:5500/docs/build/html/data_structure.html#schema>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Description
~~~~~~~~~~~

* `Description <http://127.0.0.1:5500/docs/build/html/description.html#>`_

  - `Start <http://127.0.0.1:5500/docs/build/html/description.html#start>`_

  - `Prerequiste <http://127.0.0.1:5500/docs/build/html/description.html#prerequisite>`_

  - `To do <http://127.0.0.1:5500/docs/build/html/description.html#to-do>`_

  - `Final description <http://127.0.0.1:5500/docs/build/html/description.html#final-description>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Docker
~~~~~~

* `Docker <http://127.0.0.1:5501/docs/build/html/docker.html>`_

  - `Dockerfile for Python <http://127.0.0.1:5501/docs/build/html/docker.html#dockerfile-for-python>`_

  - `Dockerfile <http://127.0.0.1:5501/docs/build/html/docker.html#dockerfile>`_

  - `docker-compose.yml <http://127.0.0.1:5501/docs/build/html/docker.html#docker-compose-yml>`_

      - `Build image <http://127.0.0.1:5501/docs/build/html/docker.html#build-image>`_

      - `Docker image <http://127.0.0.1:5501/docs/build/html/docker.html#docker-image>`_

      - `Docker image details <http://127.0.0.1:5501/docs/build/html/docker.html#docker-image-details>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Docstring
~~~~~~~~~

* `Docstring <http://127.0.0.1:5501/docs/build/html/docker.html>`_

  - `What the docstrings <http://127.0.0.1:5501/docs/build/html/docstring.html#what-the-docstrings>`_

  - `Google style <http://127.0.0.1:5501/docs/build/html/docstring.html#google-style>`_

  - `NumPy/Scipy style <http://127.0.0.1:5501/docs/build/html/docstring.html#numpy-scipy-style>`_

  - `Display docstrings <http://127.0.0.1:5501/docs/build/html/docstring.html#display-docstrings>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Documentation
~~~~~~~~~~~~~

* `Documentation <http://127.0.0.1:5500/docs/build/html/documentation.html>`_

  - `Creation <http://127.0.0.1:5500/docs/build/html/documentation.html#creation>`_

  - `Project <http://127.0.0.1:5500/docs/build/html/documentation.html#project>`_

  - `.readthedocs.yaml <http://127.0.0.1:5500/docs/build/html/documentation.html#readthedocs-yaml>`_

  - `conf.py <http://127.0.0.1:5500/docs/build/html/documentation.html#conf-py>`_

  - `Schema <http://127.0.0.1:5500/docs/build/html/data_structure.html#schema>`_

  - `requirements.txt <http://127.0.0.1:5500/docs/build/html/documentation.html#requirements-txt>`_

  - `Schema of the doc <http://127.0.0.1:5500/docs/build/html/documentation.html#schema-of-the-doc>`_


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Heroku
~~~~~~

* `Heroku <http://127.0.0.1:5501/docs/build/html/heroku.html>`_

  - `Heroku and CLI <http://127.0.0.1:5501/docs/build/html/heroku.html#heroku-and-cli>`_

  - `Signup <http://127.0.0.1:5501/docs/build/html/heroku.html#signup>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Quick start
~~~~~~~~~~~

* `Quick start <http://127.0.0.1:5500/docs/build/html/quick_start.html>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sentry
~~~~~~

* `Sentry <http://127.0.0.1:5501/docs/build/html/sentry.html>`_

  - `What is Sentry <http://127.0.0.1:5501/docs/build/html/sentry.html#what-is-sentry>`_

  - `.env <http://127.0.0.1:5501/docs/build/html/sentry.html#env>`_

  - `settings.py <http://127.0.0.1:5501/docs/build/html/sentry.html#settings-py>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Pytest-Django
~~~~~~~~~~~~~

* `Pytest-Django <http://127.0.0.1:5501/docs/build/html/test.html>`_

  - `Configuration <http://127.0.0.1:5501/docs/build/html/test.html#configuration>`_

  - `pytest.ini <http://127.0.0.1:5501/docs/build/html/test.html#pytest-ini>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

