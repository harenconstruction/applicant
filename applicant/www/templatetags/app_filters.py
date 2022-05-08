from django import template

from pm.models import ProjectCategory, Project


register = template.Library()


@register.filter(name='in_category')
def in_category(category):
    # ordering per gh41, order by state, city.
    return Project.objects.all().filter(categories=category, status='current').order_by('state', 'city')


@register.filter(name='in_past_category')
def in_past_category(category):
    # ordering per gh41, order by state, city.
    return Project.objects.all().filter(categories=category, status='past').order_by('state', 'city')
