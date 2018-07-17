from django.conf.urls import include, url
from . import views
urlpatterns = [
    url('([a-zA-z0-9_-]{3,16})/profile', views.profile_view, name='Student Profile'),
    url('([a-zA-z0-9_-]{3,16})/track_grades', views.track_grades_view, name='Track Grades'),
    url('([a-zA-z0-9_-]{3,16})/schedule', views.schedule_view, name='Student Schedule'),
    url('([a-zA-z0-9_-]{3,16})/edit-class/([0-9]{1,10})', views.edit_class_view, name='Edit Schedule'),
    url('([a-zA-z0-9_-]{3,16})/track_habits/([0-9]{1,10})', views.add_habit_score_view, name='Record Habits'),
    url('([a-zA-z0-9_-]{3,16})/track_habits', views.track_habits_view, name='Track Habits'),
    url('([a-zA-z0-9_-]{3,16})/session', views.pre_session_view, name='Pre-session'),
    url('([a-zA-z0-9_-]{3,16})/all_sessions', views.analyze_sessions_view, name='Anaylze sessions'),
    url('([a-zA-z0-9_-]{3,16})/save_session/([0-9]{1,10})', views.save_session_view, name='Pre-session'),
    url('([a-zA-z0-9_-]{3,16})/visualize', views.progress_visualization_view, name='Progress Visualization'),
]