from django.conf.urls import include, url
from . import views
urlpatterns = [
    url('([a-zA-z0-9_-]{3,16})/profile', views.profile_view, name='Student Profile'),
    url('([a-zA-z0-9_-]{3,16})/track_grades', views.track_grades_view, name='Track Grades'),
    url('([a-zA-z0-9_-]{3,16})/schedule', views.schedule_view, name='Student Schedule'),
    url('([a-zA-z0-9_-]{3,16})/edit-class/([0-9]{1,10})', views.edit_class_view, name='Edit Schedule'),
    url('([a-zA-z0-9_-]{3,16})/track_habits/([0-9]{1,10})/add/([0-9]{1,10})', views.add_habit_score_view, name='Record Habits'),
    url('([a-zA-z0-9_-]{3,16})/track_habits/([0-9]{1,10})', views.track_habits_view, name='Track Habits'),
    url('([a-zA-z0-9_-]{3,16})/track_habits', views.track_habits_redirect_view, name='Track Habits Redirect'),
    url('([a-zA-z0-9_-]{3,16})/session/([0-9]{1,10})', views.pre_session_view, name='Pre-session'),
    url('([a-zA-z0-9_-]{3,16})/session', views.session_redirect_view, name='Session Redirect'),
    url('([a-zA-z0-9_-]{3,16})/all_sessions', views.analyze_sessions_view, name='Anaylze sessions'),
    url('([a-zA-z0-9_-]{3,16})/save_session/([0-9]{1,10})', views.save_session_view, name='Pre-session'),
    url('([a-zA-z0-9_-]{3,16})/visualize', views.progress_visualization_view, name='Progress Visualization'),
    url('delete/([a-zA-z0-9_-]{3,16})', views.delete_student_view, name='Delete Student'),
    url('edit_profile/([a-zA-z0-9_-]{3,16})', views.edit_profile_view, name='Edit Profile'),
    url('([a-zA-z0-9_-]{3,16})/edit_habit/([0-9]{1,10})', views.edit_habit_view, name='Edit Habit'),
    url('([a-zA-z0-9_-]{3,16})/delete_habit/([0-9]{1,10})', views.delete_habit_view, name='Edit Habit'),
    url('forgot-password/([a-zA-z0-9_-]{3,16})', views.forgot_password_view, name='Forgot Password'),
    url('forgot-password-helper', views.forgot_password_helper, name='Forgot Password Helper'),\

]