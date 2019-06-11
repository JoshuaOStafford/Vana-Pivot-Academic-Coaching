from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('home/', views.all_student_view, name='Home Page'),
    url('setup/', views.setup_view, name='Setup'),
    url('add_student/', views.add_student_view, name='Add Student'),
    url('new_student/([a-zA-z0-9_-]{3,16})', views.create_student_account_view, name='Create Student Account'),
    url('download_CH/([a-zA-z0-9_-]{3,16})', views.download_contact_history, name='Download Content History'),
    url('download_schedule/([a-zA-z0-9_-]{3,16})', views.download_schedule, name='Download Schedule'),
]
