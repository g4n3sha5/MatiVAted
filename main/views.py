from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


def index (request):
    return render(request, "main/index.html", {})

# def renderFromFooter(request, app, view):
#
#
#     return HttpResponseRedirect(reverse(f"{view}"))
def getBaseTemplate(request, app):
    if not request.META.get('HTTP_HX_REQUEST'):
        base_template = f"{app}/base.html"
    else:
        base_template = "main/partial.html"

    return base_template