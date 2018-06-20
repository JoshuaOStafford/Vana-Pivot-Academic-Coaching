from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('/', views.quick_log, name='Quick Log')
]
