from sentry_sdk import capture_exception
from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """
    View function to display a list of lettings.

    Args:
        request: HttpRequest object representing the request made to the server.

    Returns:
        Rendered HttpResponse displaying a list of lettings.

    Raises:
        404 (Http404): If there are no lettings available.
        500 (Http500): If an unexpected error occurs while retrieving lettings.
    """
    try:
        lettings_list = Letting.objects.all()

    except Letting.DoesNotExist as e:
        capture_exception(e)
        return render(request, "404.html", status=400)

    except Exception as e:
        capture_exception(e)
        return render(request, "500.html", status=500)

    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    View function to display a specific letting.

    Args:
        request: HttpRequest object representing the request made to the server.
        letting_id: ID of the letting to be displayed.

    Returns:
        Rendered HttpResponse displaying the specific letting's title and address.

    Raises:
        404 (Http404): If the requested letting does not exist.
        500 (Http500): If an unexpected error occurs during letting retrieval.
    """
    try:
        letting = Letting.objects.get(id=letting_id)

    except Letting.DoesNotExist as e:
        capture_exception(e)
        return render(request, "404.html", status=400)

    except Exception as e:
        capture_exception(e)
        return render(request, "500.html", status=500)

    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
