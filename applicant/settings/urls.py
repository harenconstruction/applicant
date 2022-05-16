"""applicant URL Configuration"""
from django.conf import settings
from django.urls import include, re_path
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
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^application/', include('jobs.urls')),
    re_path(r'^pm/', include('pm.urls')),

    # Catch all for web content
    re_path(r'^', include('www.urls')),
]
