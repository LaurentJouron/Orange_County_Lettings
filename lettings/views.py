import logging
import sentry_sdk
from lettings.models import Letting

from django.http import Http404
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    """
    Renders the index page for lettings.

    This function retrieves a list of lettings and renders the
    "lettings/index.html" template with the list of lettings as the context.
    If there are no lettings available, it raises a 404 error.

    Args:
        request: The HTTP request object.

    Returns:
        An HTTP response containing the rendered "lettings/index.html" template.

    Raises:
        Http404: If there are no lettings available.

    Examples:
        >>> response = index(request)
    """

    try:
        lettings_list = Letting.objects.all()
    except Letting.DoesNotExist as e:
        raise Http404("There are not lettings") from e

    template = loader.get_template("lettings/index.html")
    context = {"lettings_list": lettings_list}
    return HttpResponse(template.render(context, request))


def letting(request, letting_id):
    """
    Renders the letting page for a specific letting.

    This function retrieves a letting object based on the provided letting
    ID and renders the "lettings/letting.html" template with the letting's
    title and address as the context. If the letting does not exist, it raises
    a 404 error.

    Args:
        request: The HTTP request object.
        letting_id: The ID of the letting to be rendered.

    Returns:
        A rendered HTML response containing the letting page.

    Raises:
        Http404: If the letting does not exist.

    Examples:
        >>> response = letting(request, 1)
    """

    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist as e:
        sentry_sdk.capture_message("This page does not exist!", level="error")
        logger.error("This page does not exist")
        raise Http404("This letting does not exist") from e
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
