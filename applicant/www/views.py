from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.template import RequestContext, TemplateDoesNotExist
from django.template.response import TemplateResponse

from pm.models import ProjectCategory, Project, ProjectPhoto, Slideshow


def index(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict['project_categories'] = ProjectCategory.objects.all()
    try:
        context_dict['slideshow_photos'] = Slideshow.objects.all()
    except Slideshow.DoesNotExist:
        context_dict['slideshow_photos'] = None

    return render_to_response('pages/index.html', context_dict, context)


def projects(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict['project_categories'] = ProjectCategory.objects.all().order_by('order')
    return render_to_response('pages/projects/index.html', context_dict, context)


def past_projects(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict['project_categories'] = ProjectCategory.objects.all().order_by('order')
    return render_to_response('pages/projects/past.html', context_dict, context)


def project(request, id):
    context = RequestContext(request)
    context_dict = {}

    try:
        context_dict['project'] = Project.objects.get(id=id) or None
    except Project.DoesNotExist:
        context_dict['project'] = None

    context_dict['project_photos'] = Project.objects.get(id=id).photo.all()
    context_dict['project_categories'] = ProjectCategory.objects.all()
    return render_to_response('pages/projects/project.html', context_dict, context)


def page(request, name):
    try:
        context = RequestContext(request)
        context_dict = {}
        context_dict['project_categories'] = ProjectCategory.objects.all()
        if name == 'treatment-plants.html':
            try:
                context_dict['water_project_category'] = ProjectCategory.objects.get(name='Wastewater Treatment Plants')
            except ProjectCategory.DoesNotExist:
                context_dict['water_project_category'] = None

        if name == 'pump-stations.html':
            try:
                context_dict['pumpstation_project_category'] = ProjectCategory.objects.get(name='Pump Stations')
            except ProjectCategory.DoesNotExist:
                context_dict['pumpstation_project_category'] = None

        if name == 'index.html':
            try:
                context_dict['slideshow_photos'] = Slideshow.objects.all()
            except Slideshow.DoesNotExist:
                context_dict['slideshow_photos'] = None

        return render_to_response('pages/' + name, context_dict, context)
    except TemplateDoesNotExist:
        raise Http404
