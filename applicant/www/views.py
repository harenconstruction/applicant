from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.template import RequestContext, TemplateDoesNotExist
from django.template.response import TemplateResponse


def index(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('pages/index.html', context_dict, context)


def page(request, name):
    try:
        return render(request, 'pages/' + name + '.html')
    except TemplateDoesNotExist:
        raise Http404
