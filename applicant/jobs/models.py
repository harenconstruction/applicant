from django.db import models
from django.utils import timezone
from localflavor.us.models import PhoneNumberField, USPostalCodeField

WORK_STATUS_LENGTH = 20
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


class Contact(models.Model):

    """A primary contact from the web for a job application."""

    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = USPostalCodeField()
    zipcode = models.CharField(max_length=10)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    work_eligibility_proof = models.BooleanField(blank=False, default=True, choices=BOOL_CHOICES)
    certified = models.BooleanField(blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.middle_name, self.last_name)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class EmploymentStatus(models.Model):

    """The employment status of a primary contact."""

    WORK_STATUS = (
        ('fulltime', 'Full-time'),
        ('parttime', 'Part-time'),
    )

    contact = models.ForeignKey(Contact, related_name='employmentstatus')
    legal_to_work = models.BooleanField(blank=False, default=True, choices=BOOL_CHOICES)
    available_to_work = models.CharField(max_length=WORK_STATUS_LENGTH, choices=WORK_STATUS, default=WORK_STATUS[0][0])
    start_work_date = models.DateField(verbose_name="Available for work on")
    currently_employed = models.BooleanField(blank=False, default=True, choices=BOOL_CHOICES)
    contact_employer_ok = models.BooleanField(blank=False, default=True, choices=BOOL_CHOICES)
    layoff = models.BooleanField(blank=False, default=True, choices=BOOL_CHOICES)
    filed_previously = models.BooleanField(blank=False, default=True, choices=BOOL_CHOICES)
    filed_previously_date = models.DateField(verbose_name="Previously filed on work on")
    employed_previously = models.BooleanField(blank=False, default=True, choices=BOOL_CHOICES)
    employed_previously_date = models.DateField(verbose_name="Previously employed on")
    convicted_felon = models.BooleanField(blank=False, default=True, choices=BOOL_CHOICES)
    convicted_information = models.TextField(blank=True)

    def __str__(self):
        return "{} {} {}".format(self.contact.first_name, self.contact.middle_name, self.contact.last_name)

    class Meta:
        verbose_name = 'Employment Status'
        verbose_name_plural = 'Employment Status'


class WorkExperience(models.Model):

    """A contact's past work experience contact and related information."""

    contact = models.ForeignKey(Contact, related_name='workexperience')
    company_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = USPostalCodeField()
    zipcode = models.CharField(max_length=10)
    supervisor = models.CharField(max_length=255)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    start_date = models.DateField(verbose_name="Started work on")
    start_pay = models.DecimalField(max_digits=6, decimal_places=2)
    end_date = models.DateField(verbose_name="Ended work on")
    end_pay = models.DecimalField(max_digits=6, decimal_places=2)
    job_title = models.CharField(max_length=255)
    work_information = models.TextField(blank=True)

    def __str__(self):
        return "{} {} {}".format(self.contact.first_name, self.contact.middle_name, self.contact.last_name)

    class Meta:
        verbose_name = 'Work Experience'
        verbose_name_plural = 'Work Experience'


class Education(models.Model):

    """A contact's past education information."""

    contact = models.ForeignKey(Contact, related_name='education')
    school_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = USPostalCodeField()
    zipcode = models.CharField(max_length=10)
    years_completed = models.CharField(max_length=64)
    degree_earned = models.CharField(max_length=255)
    course_description = models.TextField(blank=True)

    def __str__(self):
        return "{} {} {}".format(self.contact.first_name, self.contact.middle_name, self.contact.last_name)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'


class AdditionalInformation(models.Model):

    """A contact's qualifications, experience, and resume."""

    contact = models.ForeignKey(Contact, related_name='additionalinformation')
    summary_skills = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes')

    def __str__(self):
        return "{} {} {}".format(self.contact.first_name, self.contact.middle_name, self.contact.last_name)

    class Meta:
        verbose_name = 'Additional Information'
        verbose_name_plural = 'Additional Information'


class Reference(models.Model):

    """References for a given contact."""

    contact = models.ForeignKey(Contact, related_name='reference')
    reference_name = models.CharField(max_length=255)
    reference_location = models.CharField(max_length=255)
    reference_phone = PhoneNumberField()

    def __str__(self):
        return "{} {} {}".format(self.contact.first_name, self.contact.middle_name, self.contact.last_name)

    class Meta:
        verbose_name = 'Reference'
        verbose_name_plural = 'Reference'
