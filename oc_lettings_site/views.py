from django.shortcuts import render
from sentry_sdk import capture_message


def index(request):
    """
    Renders the index page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response with the "index.html" template.

    Examples:
        >>> response = index(request)
    """

    return render(request, "index.html")


def handler404(request, exception):
    """
    Handles the 404 page not found error.

    This function captures an error message and renders the "404.html"
    template with a status code of 404.

    Args:
        request: The HTTP request object.
        exception: The exception object representing the error.

    Returns:
        A rendered HTML response with the "404.html" template and a status
        code of 404.

    Examples:
        >>> response = handler404(request, exception)
    """

    capture_message("This page was not found.", level="error")
    return render(request, "404.html", status=404)


def handler500(request):
    """
    Handles the 500 server error.

    This function captures an error message and renders the "500.html"
    template with a status code of 500.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response with the "500.html" template and a status
        code of 500.

    Examples:
        >>> response = handler500(request)
    """

    capture_message("Page not found : error server!", level="error")
    return render(request, "500.html", status=500)
