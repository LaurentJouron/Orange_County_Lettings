.. _heroku:

Heroku
======

.. important::

      .. image:: https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white
         :alt: Heroku Badge
         :target: https://devcenter.heroku.com/categories/reference

    Parameterizations are done to a specific project. To parameterize to the other project, go to the official 
    documentation.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**************
Heroku and CLI
**************

Make sure you have a `Heroku <https://signup.heroku.com/>`_ account and the `Heroku command line interface (CLI) <https://devcenter.heroku.com/articles/heroku-cli>`_ installed on your local machine.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

******
Signup
******

To verify the installation of your `Heroku <https://dashboard.heroku.com/apps>`_ account use the following command in your terminal:

.. code-block:: console 

   heroku login

You must obtain the following result, with your credentials:

.. figure:: _static/heroku_login.png
   :scale: 50
   :align: center
   :alt: heroku login

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/heroku_login.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You must obtain the following result, with your credentials in **county-lettings/Deploy** select **Heroku Git Use Heroku CLI**

.. figure:: _static/heroku_liaison.png
   :scale: 40
   :align: center
   :alt: heroku liaison

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/heroku_liaison.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It is important to generate an API secret key to create an environment varialble in :doc:`Circle CI <circleci>`.

.. figure:: _static/heroku_api_key.png
   :scale: 40
   :align: center
   :alt: heroku api key

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/heroku_api_key.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

By going to different tabs, you can have different statistics.

.. figure:: _static/heroku_statistic_using.png
   :scale: 40
   :align: center
   :alt: heroku statistic using

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/heroku_statistic_using.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. figure:: _static/heroku_updating.png
   :scale: 40
   :align: center
   :alt: heroku updating

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/heroku_updating.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The account is configured so that each change is accessible immediately. Just push the code on GitHub and everything is done automatically.

**Before amendments**

.. figure:: _static/heroku_deployement_before.png
   :scale: 40
   :align: center
   :alt: heroku deployement

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/heroku_deployement.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**2 minutes laters**

.. figure:: _static/heroku_deployement_after.png
   :scale: 40
   :align: center
   :alt: heroku deployement

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/heroku_deployement.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. raw:: html

   <a href="https://county-lettings-dce9820cf239.herokuapp.com/" class="button">
       <img src="_static/button_open_website.png" alt="Report button" width="200" height="100" />
   </a>
