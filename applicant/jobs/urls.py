from django.urls import include, re_path

from jobs.views import index_form, applicant_thanks

from jobs.forms import (ContactForm,
                        EmploymentStatusForm,
                        WorkExperienceFormset,
                        EducationFormset,
                        AdditionalInformationForm,
                        ReferenceFormset,
                        CompleteForm)
from jobs.views import ApplicationWizard, all

FORMS = [("contact", ContactForm),
         ("employmentstatus", EmploymentStatusForm),
         ("workexperience", WorkExperienceFormset),
         ("education", EducationFormset),
         ("additionalinformation", AdditionalInformationForm),
         ("reference", ReferenceFormset),
         ("complete", CompleteForm)]

urlpatterns = [
    # url(r'^index.html$', index_form, name='index'),
    # url(r'^$', index_form, name='index'),

    # application
    re_path(r'^index.html$', ApplicationWizard.as_view(FORMS), name='application'),
    re_path(r'^$', ApplicationWizard.as_view(FORMS), name='application'),
    re_path(r'^thanks$', applicant_thanks, name='thanks'),
    re_path(r'^(?P<name>.*)', all),
    re_path(r'^$', ApplicationWizard.as_view(FORMS), name='application'),
]
