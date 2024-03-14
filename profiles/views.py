from sentry_sdk import capture_exception
from django.shortcuts import render
from .models import Profile


def index(request):
    """
    View function to display a user's profile.

    Args:
        request: HttpRequest object representing the request made to the server.
        username: Username of the user whose profile is being accessed.

    Returns:
        Rendered HttpResponse displaying the user's profile.

    Raises:
        404 (Http404): If the requested profile does not exist.
        500 (Http500): If an unexpected error occurs during profile retrieval.
    """
    try:
        profiles_list = Profile.objects.all()

    except Profile.DoesNotExist as e:
        capture_exception(e)
        return render(request, "404.html", status=400)

    except Exception as e:
        capture_exception(e)
        return render(request, "500.html", status=500)

    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    View function to display a user's profile.

    Args:
        request: HttpRequest object representing the request made to the server.
        username: Username of the user whose profile is being accessed.

    Returns:
        Rendered HttpResponse displaying the user's profile.

    Raises:
        404 (Http404): If the requested profile does not exist.
        500 (Http500): If an unexpected error occurs during profile retrieval.
    """
    try:
        profile = Profile.objects.get(user__username=username)

    except Profile.DoesNotExist as e:
        capture_exception(e)
        return render(request, "404.html", status=400)

    except Exception as e:
        capture_exception(e)
        return render(request, "500.html", status=500)

    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
