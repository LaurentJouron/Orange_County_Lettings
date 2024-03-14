import logging
from sentry_sdk import capture_exception
from lettings.models import Letting

from django.http import Http404
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    try:
        lettings_list = Letting.objects.all()
    except Letting.DoesNotExist as e:
        capture_exception(e)
        return render(request, "404.html", status=400)

    except Exception as e:
        capture_exception(e)
        return render(request, "500.html", status=500)
    template = loader.get_template("lettings/index.html")
    context = {"lettings_list": lettings_list}
    return HttpResponse(template.render(context, request))


def letting(request, letting_id):
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
