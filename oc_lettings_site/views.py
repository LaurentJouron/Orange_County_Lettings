from django.shortcuts import render
from sentry_sdk import capture_exception


def index(request):
    try:
        return render(request, "index.html")

    except Exception as e:
        capture_exception(e)
        return render(request, "500.html", status=500)
