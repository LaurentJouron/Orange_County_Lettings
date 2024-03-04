.. _docstring:

**Docstring**
=============

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*******************
What the docstrings
*******************

💡Python docstrings are documentation strings that are embedded directly into the source code of a function, 
class, or module. They are used to provide clear and concise information about the 
purpose with which they are associated. Docstrings can be accessed via the ``_doc_`` attribute of the relevant object and 
are used to automatically generate more detailed documentation using tools like Sphinx.

These docstring styles allow developers to quickly understand how to use a function or class without having to examine 
the source code, making it easier to collaborate and maintain the code.

*There are several styles of docstrings in Python, but two of the most common are:*

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

************
Google style
************

.. image:: https://img.shields.io/badge/docstrings-google-blue.svg?style=for-the-badge&logo=google&logoColor=white
   :alt: Google Docstrings Badge
   :target: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html


⚙️ Google

.. code-block:: Python

        def addition(a, b):
            """
            This function takes two numbers as input and returns their sum.

            Args:
                a (int): The first number.
                b (int): The second number.

            Returns:
                int: The sum of the two numbers.
            """
            return a + b

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****************
NumPy/Scipy style
*****************

.. image:: https://img.shields.io/badge/docstrings-numpy/scipy-blue.svg?style=for-the-badge&logo=python&logoColor=white
   :alt: NumPy/SciPy Docstrings Badge
   :target: https://numpydoc.readthedocs.io/en/latest/format.html

This style is similar to the Google style but uses specific sections to describe parameters, return values, etc. Here’s an example:

⚙️ NumPy/SciPy

.. code-block:: Python

        def multiply_matrix(matrix, scalar):
            """
            Multiply a matrix by a scalar.

            Parameters
            ----------
            matrix : numpy.ndarray
                The input matrix to be multiplied.
            scalar : int or float
                The scalar value to multiply the matrix by.

            Returns
            -------
            numpy.ndarray
                The resulting matrix after multiplication.
            """
            return matrix * scalar


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

******************
Display docstrings
******************

To affcicher the documentation of a function, class or method, it is necessary to write the name of it, followed by ``.__doc__``

.. code-block:: Python

        print(addition.__doc__)


💡Results for google style

.. code-block:: Python

        This function takes two numbers as input and returns their sum.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The sum of the two numbers.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. code-block:: Python

        print(multiply_matrix.__doc__)

💡Results for NumPy/Scipy style

.. code-block:: Python

        Multiply a matrix by a scalar.

        Parameters
        ----------
        matrix : numpy.ndarray
            The input matrix to be multiplied.
        scalar : int or float
            The scalar value to multiply the matrix by.

        Returns
        -------
        numpy.ndarray
            The resulting matrix after multiplication. 
