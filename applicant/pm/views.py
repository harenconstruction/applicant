from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist


def all(request, name):
    context_dict = {}
    try:
        if name:
            return render(request, './pages/' + name, context_dict)
        else:
            return render(request, './pages/index.html', context_dict)
    except TemplateDoesNotExist:
        raise Http404
