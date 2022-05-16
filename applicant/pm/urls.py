from django.urls import include, re_path

from pm.views import all


urlpatterns = [
    re_path(r'^pm/(?P<name>.*)', all),
]
