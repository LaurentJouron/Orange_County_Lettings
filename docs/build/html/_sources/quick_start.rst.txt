.. _quick_start:

Quick start
===========

.. note::

   This way of installation is the simplest. On the other hand, this use is local, which means that nothing is found 
   on the internet and is accessible only on the computer you are using.

There are several solutions to install the project. The easiest for quick use is as follows:

.. rubric:: ⚙️ Clone

.. code-block:: console

   git clone https://github.com/LaurentJouron/Orange_County_Lettings.git

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. rubric:: ⏩️ Change directory in the project:

.. code-block:: console

   cd Orange_County_Lettings

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. rubric:: ⚙️ Create virtual environment folder

.. code-block:: console

   mkdir .venv

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. caution:: I use pipenv but all commands are functional with pip

.. rubric:: ⚙️ Install virtual environment

.. code-block:: console

   pipenv install

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. rubric:: ⏩️ Activate environment

.. code-block:: console

   pipenv shell

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. rubric:: ⏩️ Launch local project

.. code-block:: console
   
   python manage.py runserver

.. warning:: This button is only functional if the project is activated according to the above process. If this is the case ``click`` on it, otherwise it leads to an **error page**.

.. raw:: html

   <a href="http://localhost:8000" class="button" target=_blank>
       <img src="_static/button_open_website.png" alt="Bouton" width="200" height="100" />
   </a>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. rubric:: 🔚 Quit

To leave the server and stop any intervention on the website.

.. code-block:: console

   ctrl + c
