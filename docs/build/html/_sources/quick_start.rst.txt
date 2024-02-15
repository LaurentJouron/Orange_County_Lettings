.. _quick_start:

**Quick start**
===============

There are several solutions to install the project. The easiest for quick use is as follows:

Start by ``cloning the project`` with this command:


.. code-block:: console

   git clone https://github.com/LaurentJouron/Orange_County_Lettings.git


Place yourself ``inside the project``:

.. code-block:: console

   cd Orange_County_Lettings


Create a ``.venv`` folder to access the ``virtual environment``

.. code-block:: console

   mkdir .venv


Install the ``necessary environment``

.. code-block:: console

   pipenv install

or

.. code-block:: console

   pip install


``Activate`` the virtual environment

.. code-block:: console

   pipenv shell

or

.. code-block:: console

   pip shell


It remains only to ``launch the project`` to be able to browse it.

.. code-block:: console
   
   python manage.py runserver


`Open the website <http://localhost:8000>`_


.. note::
   This way of installation is the simplest. On the other hand, this use is local, which means that nothing is found 
   on the internet and is accessible only on the computer you are using.
