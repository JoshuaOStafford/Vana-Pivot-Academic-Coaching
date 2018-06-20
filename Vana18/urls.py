from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^marni', include('Coach.urls')),
    url(r'^student', include('student.urls')),
    url(r'^reports', include('metrics.urls')),
    url(r'^admin', admin.site.urls),
]
