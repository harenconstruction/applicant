from django.contrib import admin
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

from jobs.models import Contact, EmploymentStatus, WorkExperience, Education, AdditionalInformation, Reference

admin.site.register(Contact)
admin.site.register(EmploymentStatus)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(AdditionalInformation)
admin.site.register(Reference)
