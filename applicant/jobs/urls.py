from django.conf.urls import url
from jobs.views import index_form

from jobs.forms import ContactForm, EmploymentStatusForm, WorkExperienceForm, EducationForm, AdditionalInformationForm, ReferenceForm
from jobs.views import ApplicationWizard

FORMS = [("contact", ContactForm),
         ("employmentstatus", EmploymentStatusForm),
         ("workexperience", WorkExperienceForm),
         ("education", EducationForm),
         ("additionalinformation", AdditionalInformationForm),
         ("reference", ReferenceForm)]

urlpatterns = [
    url(r'^index.html$', index_form, name='index'),
    url(r'^$', index_form, name='index'),

    # application
    url(r'^application/$', ApplicationWizard.as_view(FORMS), name='application'),
]
