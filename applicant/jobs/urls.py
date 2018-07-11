from django.conf.urls import url
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
    url(r'^index.html$', ApplicationWizard.as_view(FORMS), name='application'),
    url(r'^$', ApplicationWizard.as_view(FORMS), name='application'),
    url(r'^thanks$', applicant_thanks, name='thanks'),
    url(r'^(?P<name>.*)', all),
    url(r'^$', ApplicationWizard.as_view(FORMS), name='application'),
]
