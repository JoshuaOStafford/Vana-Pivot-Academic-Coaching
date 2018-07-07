from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Vana18.forms import LoginForm

urlpatterns = [
    url(r'^login$', auth_views.login, {'template_name': 'registration/login.html', 'authentication_form': LoginForm}),
    url(r'^logout$', auth_views.logout, {'template_name': 'registration/login.html'}),
    url(r'^marni', include('Coach.urls')),
    url(r'^student', include('student.urls')),
    url(r'^admin', admin.site.urls),
]
