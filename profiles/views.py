import logging
import sentry_sdk
from django.http import Http404
from django.shortcuts import render
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist as e:
        sentry_sdk.capture_message("This page does not exist!", level="error")
        logger.error("This page does not exist")
        raise Http404("This profile does not exist") from e
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
