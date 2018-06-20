from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('/log', views.quick_log, name='Quick Log'),
    url('/view', views.view_scores, name='View Scores'),

]
