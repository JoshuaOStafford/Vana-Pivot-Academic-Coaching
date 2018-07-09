from django.conf.urls import include, url
from . import views
urlpatterns = [
    url('([a-zA-z0-9_-]{3,16})/profile', views.profile_view, name='Student Profile'),
    url('([a-zA-z0-9_-]{3,16})/track_grades', views.track_grades_view, name='Track Grades'),
    url('([a-zA-z0-9_-]{3,16})/schedule', views.schedule_view, name='Student Schedule'),
    url('track_habits', views.track_habits_view, name='Track Habits'),
    url('pre_session', views.pre_session_view, name='Pre-session'),
    url('visualizations', views.progress_visualization_view, name='Progress Visualization'),
]