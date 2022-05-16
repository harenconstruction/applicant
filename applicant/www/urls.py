from django.urls import re_path

from www import views


urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^projects$', views.projects),
    re_path(r'^projects/past$', views.past_projects),
    re_path(r'^project/(?P<id>\d+)$', views.project),
    re_path(r'^(?P<name>.*)', views.page),
]
