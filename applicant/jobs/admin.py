import re

from django.contrib import admin
from django.contrib.admin import helpers
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.template.response import TemplateResponse

from jobs.models import Contact, EmploymentStatus, WorkExperience, Education, AdditionalInformation, Reference
from jobs.email import send_templated_email

# admin.site.register(EmploymentStatus)
# admin.site.register(WorkExperience)
# admin.site.register(Education)
# admin.site.register(AdditionalInformation)
# admin.site.register(Reference)


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

    model = Contact
    list_filter = ('created_at', 'updated_at', 'state')
    list_display = ('__str__', 'created_at')
    search_fields = ['first_name','middle_name','last_name','email','phone',]

    def email_contacts(self, request, queryset):
        if request.POST.get('post'):
            if 'email' in request.POST:
                for email in re.split(r'[, ]*', request.POST['email']):
                    for i in queryset:
                        if i.first_name:
                            self.message_user(request, "Sending '{}' to {}".format(i.first_name, email))
                            send_templated_email('Job application contact', 'email/applicant_email.html', {"contact": i, "message": request.POST['message']}, email,
                                                    sender=None, bcc=None, fail_silently=True, files=None)

                self.message_user(request, "Contact information emailed successfully.")
            else:
                self.message_user(request, "No email provided to forward application to.")
        else:
            context = {
                'title': ("Send job application by e-mail:"),
                'queryset': queryset,
                'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
            }

            return TemplateResponse(request, 'admin/email_action.html',
                                    context, current_app=self.admin_site.name)

    actions = [email_contacts]


admin.site.register(Contact, ContactAdmin)
