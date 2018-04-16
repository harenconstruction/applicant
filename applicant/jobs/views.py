import datetime
import os

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import TemplateDoesNotExist

from formtools.wizard.views import SessionWizardView

from config import settings
from jobs.email import send_templated_email
from jobs.models import WorkState


TEMPLATES = {"contact": "jobs/contact.html",
             "employmentstatus": "jobs/employmentstatus.html",
             "workexperience": "jobs/workexperience.html",
             "education": "jobs/education.html",
             "additionalinformation": "jobs/additionalinformation.html",
             "reference": "jobs/reference.html",
             "complete": "jobs/complete.html"}


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


def applicant_thanks(request):
    context_dict = {}

    return render(request, './jobs/thanks.html', context_dict)


class ApplicationWizard(SessionWizardView):

    file_storage = FileSystemStorage(location=os.path.join(settings.TEMP_PATH, 'file_uploads'))

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, form_dict, **kwargs):
        form_data = process_form_data(form_list)

        contact = form_dict['contact'].save()
        complete = form_dict['complete']
        contact.certified = complete.cleaned_data['certified']
        contact.save()

        employmentstatus = form_dict['employmentstatus']
        employmentstatus.fields['states_available_work'].queryset = WorkState.objects.all()
        employmentstatus_object = employmentstatus.save(commit=False)
        employmentstatus_object.contact_id = contact.id
        employmentstatus_object.save()
        employmentstatus.save_m2m();

        for workexperience in form_dict['workexperience']:
            workexperience = workexperience.save(commit=False)
            workexperience.contact_id = contact.id
            workexperience.save()

        for education in form_dict['education']:
            education = education.save(commit=False)
            education.contact_id = contact.id
            education.save()

        additionalinformation = form_dict['additionalinformation'].save(commit=False)
        additionalinformation.contact_id = contact.id
        additionalinformation.save()

        for reference in form_dict['reference']:
            reference = reference.save(commit=False)
            reference.contact_id = contact.id
            reference.save()

        # email this crud.
        # application@harenconstruction.com
        if additionalinformation.resume:
            resume = '/home/applicant' + additionalinformation.resume.url
            send_templated_email('Job application contact', 'email/applicant_email.html', {"contact": contact, "message": "A new job application has been created."}, "application@harenconstruction.com",
                                    sender=None, bcc=None, fail_silently=True, files=resume)
        else:
            send_templated_email('Job application contact', 'email/applicant_email.html', {"contact": contact, "message": "A new job application has been created."}, "application@harenconstruction.com",
                                    sender=None, bcc=None, fail_silently=True)


        return HttpResponseRedirect('thanks', {'form_data': form_data})


def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]

    # email haren?


    return form_data
