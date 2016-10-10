"""applicant URL Configuration"""
from django.conf.urls import include, url
from django.contrib import admin

from jobs import views

urlpatterns = [
    url(r'^', include('jobs.urls')),
]

urlpatterns += [
    url(r'^admin/', admin.site.urls),

    url(r'^(?P<name>.*)', views.all),
]
