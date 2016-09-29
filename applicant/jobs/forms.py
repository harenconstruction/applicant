from django import forms
from django.template.loader import render_to_string
from localflavor.us.forms import USZipCodeField

from jobs.models import Contact, EmploymentStatus, WorkExperience, Education, AdditionalInformation, Reference


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
            'start_work_date': forms.DateInput(attrs={'class':'datepicker'})
        }
        fields = ('legal_to_work', 'available_to_work', 'start_work_date',
                  'currently_employed', 'contact_employer_ok', 'layoff',
                  'filed_previously', 'filed_previously_date',
                  'employed_previously', 'employed_previously_date',
                  'convicted_felon', 'convicted_information',)


class WorkExperienceForm(forms.ModelForm):

    class Meta:
        model = WorkExperience
        fields = ('company_name', 'city', 'state', 'zipcode', 'supervisor',
                  'phone', 'email', 'start_date', 'start_pay', 'end_date',
                  'end_pay', 'job_title', 'work_information',)


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('school_name', 'city', 'state', 'zipcode', 'years_completed',
                  'degree_earned', 'course_description',)


class AdditionalInformationForm(forms.ModelForm):

    class Meta:
        model = AdditionalInformation
        fields = ('summary_skills', 'resume',)


class ReferenceForm(forms.ModelForm):

    class Meta:
        model = Reference
        fields = ('reference_name', 'reference_location', 'reference_phone',)
