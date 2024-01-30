import logging
import sentry_sdk
from django.http import Http404
from django.shortcuts import render
from .models import Letting
from django.template import loader
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    try:
        lettings_list = Letting.objects.all()
    except Letting.DoesNotExist as e:
        raise Http404("There are not lettings") from e

    template = loader.get_template("lettings/index.html")
    context = {"lettings_list": lettings_list}
    return HttpResponse(template.render(context, request))


def letting(request, letting_id):
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
