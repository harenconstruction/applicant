from django.conf.urls import url


from pm.views import all


urlpatterns = [
    url(r'^pm/(?P<name>.*)', all),
]
