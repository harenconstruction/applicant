from django.conf.urls import url


from www import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^projects$', views.projects),
    url(r'^projects/past$', views.past_projects),
    url(r'^project/(?P<id>\d+)$', views.project),
    url(r'^(?P<name>.*)', views.page),
]
