.. _error:

**Error**
=========

.. important::
    
    The configuration below is very inspired by the official file `sentry http_errors <https://docs.sentry.io/platforms/python/integrations/django/http_errors/>`_ 


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*********
404 Error
*********

⚠️ 404 Error - Page not found

404 is one of the most common HTTP errors and occurs when a user tries to access a 
resource (web page, file, etc.) that does not exist on the server.
This error is usually displayed when the requested URL is not found in the application or on the web server.
The 404 error is often called **Page not found** because it indicates that the requested resource is not available.
In a Django application, a custom 404 error page can be displayed to guide users when they encounter this error.


💡 handler404

In Django, handler404 is a variable that specifies the function or view that will be called when Django 
encounters a 404 error, that is, a page that is not found.

Here’s how to describe it and how it is used in urls.py:

.. console:: Python

    # 404 erreur: page not found
    handler404 = views.handler404

💡 Description:

handler404 is a variable used in the urls.py file to specify the function or view that will be 
executed when Django encounters a 404 error. This error occurs when a user tries to access a URL 
that does not exist in your Django application.

💡 Usage:

To use handler404, you must assign to a view or function that handles the display of the 404 error 
custom page. This view or function must be defined in a views.py file.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*********
500 Error
*********

⚠️ 500 Error - Internal server error:

Error 500, also known as "Internal Server Error", occurs when an error occurs on the server side that 
prevents the HTTP response from being generated correctly.
This error may be due to various problems, such as programming errors in the application code, server 
configuration problems, database errors, etc.
Unlike the 404 error which indicates a problem with the user’s request, the 500 error indicates a problem 
with the server itself.
A custom 500 error page can be used to inform users that the server is experiencing temporary difficulties 
and to provide instructions on what they can do, such as trying again later or contacting the site 
administrator.

💡 handler500 - Description:

handler500 is a variable used in Django’s urls.py file to specify the function or view that will be 
executed when Django encounters a 500 error, also known as the "Server Error" error. This error occurs 
when Django encounters an internal server error.

.. console:: Python

    # 500 erreur: Server error
    handler500 = views.handler500


💡 Usage:

To use handler500, it must be assigned to a view or function that handles the display of the 500 error 
custom page. This view or function must be defined in your views.py file.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*******
Summary
*******

💡 In summary, the 404 error indicates that the requested resource does not exist, while the 500 error 
indicates an internal server error. In both cases, it is important to provide custom error pages to 
guide users and improve their website experience.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
