from django.conf.urls import include, url
from . import views
urlpatterns = [
    url('profile', views.profile_view, name='Student Profile'),
    url('track_grades', views.track_grades_view, name='Track Grades'),
    url('schedule', views.schedule_view, name='Student Schedule'),
    url('track_habits', views.track_habits_view, name='Track Habits'),
    url('pre_session', views.pre_session_view, name='Pre-session'),
    url('visualizations', views.progress_visualization_view, name='Progress Visualization'),
]