from django.shortcuts import render
from django.http import HttpResponseRedirect


def change_theme(request, **kwargs):
    if "is_dark_theme" in request.session:
        request.session["is_dark_theme"] = not request.session["is_dark_theme"]
    else:
        request.session["is_dark_theme"] = True
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
