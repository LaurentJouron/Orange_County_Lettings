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

.. rubric:: Install Sphinx

.. code-block:: console

   pipenv install sphinx

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. rubric:: Creating the documentation layout

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

.. rubric:: build/
    
* An empty directory (for now) that will hold the rendered documentation.


.. rubric:: make.bat and Makefile

* Convenience scripts to simplify some common Sphinx operations, such as rendering the content.


.. rubric:: source/conf.py

* A Python script holding the configuration of the Sphinx project. It contains the project name and release 
you specified to sphinx-quickstart, as well as some extra configuration keys.


.. rubric:: source/index.rst
    
* The root document of the project, which serves as welcome page and contains the root of the “table of contents tree” (or toctree).

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. rubric:: Build docs/build/

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

.. rubric:: Position yourself in the docs folder

.. code-block:: console

   cd docs


.. rubric:: make html

This command must be retained because this command will be repeated with each modification.

.. code-block:: console

   .\make html

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****************
.readthedocs.yaml
*****************

To realize this documentation I used this configuration for the file ``.readthedocs.yaml``

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

.. code-block:: txt

    Sphinx==7.2.6
    sphinx-rtd-theme==1.3.0
    sphinx-bootstrap-theme
    sphinx-copybutton
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****************
Schema of the doc
*****************

* `Description <http://127.0.0.1:5500/docs/build/html/description.html#>`_

  - `Start <http://127.0.0.1:5500/docs/build/html/description.html#start>`_

  - `Prerequiste <http://127.0.0.1:5500/docs/build/html/description.html#prerequisite>`_

  - `To do <http://127.0.0.1:5500/docs/build/html/description.html#to-do>`_

  - `Final description <http://127.0.0.1:5500/docs/build/html/description.html#final-description>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* `Quick start <http://127.0.0.1:5500/docs/build/html/quick_start.html>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* `Data structure <http://127.0.0.1:5500/docs/build/html/data_structure.html>`_

  - `Specifications <http://127.0.0.1:5500/docs/build/html/data_structure.html#need-for-the-specifications>`_

  - `Address <http://127.0.0.1:5500/docs/build/html/data_structure.html#address>`_

  - `Lettings <http://127.0.0.1:5500/docs/build/html/data_structure.html#lettings>`_

  - `Profile <http://127.0.0.1:5500/docs/build/html/data_structure.html#profile>`_

  - `Schema <http://127.0.0.1:5500/docs/build/html/data_structure.html#schema>`_

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* `Documentation <http://127.0.0.1:5500/docs/build/html/documentation.html>`_

  - `Creation <http://127.0.0.1:5500/docs/build/html/documentation.html#creation>`_

  - `Project <http://127.0.0.1:5500/docs/build/html/documentation.html#project>`_

  - `.readthedocs.yaml <http://127.0.0.1:5500/docs/build/html/documentation.html#readthedocs-yaml>`_

  - `conf.py <http://127.0.0.1:5500/docs/build/html/documentation.html#conf-py>`_

  - `Schema <http://127.0.0.1:5500/docs/build/html/data_structure.html#schema>`_

  - `requirements.txt <http://127.0.0.1:5500/docs/build/html/documentation.html#requirements-txt>`_

  - `Schema of the doc <http://127.0.0.1:5500/docs/build/html/documentation.html#schema-of-the-doc>`_
