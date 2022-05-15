import uuid
import os

from django.db import models

from localflavor.us.models import USPostalCodeField


PROJECT_STATUS_LENGTH = 10
PROJECT_STATUS_CHOICES = (('current', 'Current'), ('past', 'Past'),
                          ('archived', 'Archived'))


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('project_photos', filename)


class ProjectCategory(models.Model):

    """A project category, which is associated n:m."""

    name = models.CharField(unique=True, max_length=64)
    order = models.IntegerField('Position', default=0)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Project Cateogry'
        verbose_name_plural = 'Project Categories'


class Project(models.Model):

    """A construction project with attributes such as location, cost, principle engineer, description."""

    name = models.CharField(unique=True, max_length=64)
    description = models.TextField(blank=True)
    engineer = models.CharField(max_length=64, blank=True, null=True)
    owner = models.CharField(max_length=64, blank=True, null=True)
    location = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = USPostalCodeField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    cost_description = models.TextField(null=True, blank=True)
    project_timeframe = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(ProjectCategory, related_name='projects')
    status = models.CharField(max_length=PROJECT_STATUS_LENGTH, choices=PROJECT_STATUS_CHOICES, default=PROJECT_STATUS_CHOICES[0][0])

    def __str__(self):
        return "{} {}".format(self.name, self.location)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class ProjectPhoto(models.Model):

    project = models.ForeignKey(Project, related_name='photo')
    photo = models.ImageField(blank=True, upload_to=get_file_path)
    title = models.CharField(blank=True, null=True, max_length=64)

    def __str__(self):
        return "{}: {}".format(self.project.name, self.title)

    def image_tag(self):
        return u'<img src="%s" width="200" height="200" />' % self.photo.url

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'Project Photo'
        verbose_name_plural = 'Project Photos'


class Slideshow(models.Model):

    project_photo = models.ManyToManyField(ProjectPhoto, related_name='project_photo')

    class Meta:
        verbose_name = 'Slideshow photo'
        verbose_name_plural = 'Slideshow photos'
