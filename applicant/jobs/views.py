import datetime
import os

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import TemplateDoesNotExist

from formtools.wizard.views import SessionWizardView

from config import settings

TEMPLATES = {"contact": "jobs/contact.html",
             "employmentstatus": "jobs/employmentstatus.html",
             "workexperience": "jobs/workexperience.html",
             "education": "jobs/education.html",
             "additionalinformation": "jobs/additionalinformation.html",
             "reference": "jobs/reference.html"}


def all(request, name):
    context_dict = {}
    try:
        if name:
            return render(request, './pages/' + name, context_dict)
        else:
            return render(request, './pages/index.html', context_dict)
    except TemplateDoesNotExist:
        raise Http404


def index_form(request):
    context_dict = {}

    return render(request, './pages/index.html', context_dict)


class ApplicationWizard(SessionWizardView):

    file_storage = FileSystemStorage(location=os.path.join(settings.TEMP_PATH, 'file_uploads'))

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        return HttpResponseRedirect('jobs/thanks.html', {'form_data': form_data})


def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]

    # email haren?


    return form_data
