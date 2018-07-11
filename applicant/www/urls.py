from django.conf.urls import url


from www import views


urlpatterns = [
    url(r'^(?P<name>.*)', views.page),
]
