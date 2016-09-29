from django.contrib import admin
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

from jobs.models import Contact, EmploymentStatus, WorkExperience, Education, AdditionalInformation, Reference

admin.site.register(EmploymentStatus)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(AdditionalInformation)
admin.site.register(Reference)


class EmploymentStatusInline(admin.TabularInline):
    model = EmploymentStatus
    max_num = 1
    extra = 0


class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience


class EducationInline(admin.TabularInline):
    model = Education


class AdditionalInformationInline(admin.TabularInline):
    model = AdditionalInformation
    max_num = 1
    extra = 0


class ReferenceInline(admin.TabularInline):
    model = Reference
    max_num = 3
    extra = 0


class ContactAdmin(admin.ModelAdmin):
    inlines = [
        EmploymentStatusInline,
        WorkExperienceInline,
        EducationInline,
        AdditionalInformationInline,
        ReferenceInline,
    ]


admin.site.register(Contact, ContactAdmin)
