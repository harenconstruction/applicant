from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.template import RequestContext, TemplateDoesNotExist
from django.template.response import TemplateResponse
from django.urls import reverse

from pm.models import ProjectCategory, Project, ProjectPhoto, Slideshow


def index(request):
    context_dict = {}
    context_dict['project_categories'] = ProjectCategory.objects.all()
    try:
        context_dict['slideshow_photos'] = Slideshow.objects.all()
    except Slideshow.DoesNotExist:
        context_dict['slideshow_photos'] = None

    return render(request, 'pages/index.html', context_dict)


def projects(request):
    context_dict = {}
    context_dict['project_categories'] = ProjectCategory.objects.all().order_by('order')
    return render(request, 'pages/projects/index.html', context_dict)


def past_projects(request):
    context_dict = {}
    context_dict['project_categories'] = ProjectCategory.objects.all().order_by('order')
    return render(request, 'pages/projects/past.html', context_dict)


def project(request, id):
    context_dict = {}

    try:
        context_dict['project'] = Project.objects.get(id=id) or None
    except Project.DoesNotExist:
        context_dict['project'] = None

    context_dict['project_photos'] = Project.objects.get(id=id).photo.all()
    context_dict['project_categories'] = ProjectCategory.objects.all().order_by('order')
    return render(request, 'pages/projects/project.html', context_dict)


def page(request, name):
    try:
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

        return render(request, 'pages/' + name, context_dict)
    except TemplateDoesNotExist:
        raise Http404
