"""applicant URL Configuration"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

import jobs
import pm
import www
# from www import views

urlpatterns = []

# handle debug serving of media files

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^application/', include('jobs.urls')),
    url(r'^pm/', include('pm.urls')),

    # Catch all for web content
    url(r'^', include('www.urls')),
]
