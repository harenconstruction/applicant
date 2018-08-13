from django import forms
from django.forms import formset_factory
from django.template.loader import render_to_string
from localflavor.us.forms import USZipCodeField

from jobs.models import (Contact, WorkState, EmploymentStatus, WorkExperience,
                         Education, AdditionalInformation, Reference)


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        widgets = {
            'work_eligibility_proof': forms.RadioSelect
        }
        fields = ('first_name', 'middle_name', 'last_name',
                  'address', 'address2', 'city', 'state', 'zipcode',
                  'phone', 'email', 'work_eligibility_proof',)


class EmploymentStatusForm(forms.ModelForm):

    filed_previously_date = forms.DateField(required=False)
    employed_previously_date = forms.DateField(required=False)

    class Meta:
        model = EmploymentStatus
        widgets = {
            'legal_to_work': forms.RadioSelect,
            'available_to_work': forms.RadioSelect,
            'currently_employed': forms.RadioSelect,
            'contact_employer_ok': forms.RadioSelect,
            'layoff': forms.RadioSelect,
            'filed_previously': forms.RadioSelect,
            'employed_previously': forms.RadioSelect,
            'convicted_felon': forms.RadioSelect,
            'start_work_date': forms.DateInput(attrs={'class':'datepicker'}),
            'states_available_work': forms.CheckboxSelectMultiple,
            'work_skills': forms.CheckboxSelectMultiple
        }
        fields = ('legal_to_work', 'available_to_work',
                  'start_work_date', 'currently_employed', 'contact_employer_ok',
                  'layoff', 'filed_previously', 'filed_previously_date',
                  'employed_previously', 'employed_previously_date',
                  'convicted_felon', 'convicted_information',
                  'states_available_work', 'work_skills',
                  )


class WorkExperienceForm(forms.ModelForm):

    class Meta:
        model = WorkExperience
        fields = ('company_name', 'city', 'state', 'zipcode', 'supervisor',
                  'phone', 'email', 'start_date', 'start_pay', 'start_pay_cycle',
                  'end_date', 'end_pay', 'end_pay_cycle', 'job_title',
                  'work_information',)

# http://stackoverflow.com/questions/22770993/can-a-step-be-repeated-in-django-1-6-form-wizard
# https://docs.djangoproject.com/en/1.10/topics/forms/formsets/
# https://news.ycombinator.com/item?id=5670997
# https://github.com/elo80ka/django-dynamic-formset/blob/master/docs/usage.rst
WorkExperienceFormset = formset_factory(WorkExperienceForm, extra=0)


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('school_name', 'city', 'state', 'zipcode', 'years_completed',
                  'degree_earned', 'course_description',)


EducationFormset = formset_factory(EducationForm, extra=0)


class AdditionalInformationForm(forms.ModelForm):

    class Meta:
        model = AdditionalInformation
        fields = ('summary_skills', 'resume',)


class ReferenceForm(forms.ModelForm):

    class Meta:
        model = Reference
        fields = ('reference_name', 'reference_location', 'reference_phone',)


ReferenceFormset = formset_factory(ReferenceForm, extra=3)


''' This class should not be saved, rather it only copies the field `certified`
for later use in ContactForm.'''

class CompleteForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('certified',)
