.. _test:

**Pytest-Django**
=================

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

pytest-django is a plugin for `pytest <https://docs.pytest.org/en/8.0.x/>`_  that provides a set of useful tools 
for testing `Django <https://www.djangoproject.com/>`_ applications and projects.

.. warning::

    The configuration below is very inspired by the official file `pytest-django <https://pytest-django.readthedocs.io/en/latest/>`_ 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

***********
Quick start
***********

.. code-block:: console

   pip install pytest-django

Make sure ``DJANGO_SETTINGS_MODULE`` is 
defined (`see Configuring Django settings <https://pytest-django.readthedocs.io/en/latest/configuring_django.html#configuring-django-settings>`_) 
and make your tests discoverable (`see My tests are not being found. Why? <https://pytest-django.readthedocs.io/en/latest/faq.html#faq-tests-not-being-picked-up>`_):

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**********
pytest.ini
**********

.. code-block:: python

    [pytest]
    DJANGO_SETTINGS_MODULE = test.settings
    # -- recommended but optional:
    python_files = tests.py test_*.py *_tests.py

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**********
First test
**********

Run your tests with ``pytest``:

.. code-block:: python

    pytest

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*******
Results
*******


