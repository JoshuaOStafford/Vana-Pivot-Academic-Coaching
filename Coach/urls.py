from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('home/', views.all_student_view, name='Home Page')
]
