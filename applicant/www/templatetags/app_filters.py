from django import template

from pm.models import ProjectCategory, Project


register = template.Library()


@register.filter(name='in_category')
def in_category(category):
    return Project.objects.all().filter(categories=category, status='current')


@register.filter(name='in_past_category')
def in_past_category(category):
    return Project.objects.all().filter(categories=category, status='past')
