from django.shortcuts import render, redirect
from student.models import Student, AcademicCoach, School, Parent, Contact, Class, ClassGrade, Habit, HabitScore, Session
from student.helpers import student_has_no_classes, is_coach
from datetime import date, timedelta


def profile_view(request, username):
    page = 'profile'
    coach = is_coach(request)
    no_classes = student_has_no_classes(request)
    student = Student.objects.get(username=username)
    parents = []
    for parent in student.parent_set.all():
        parents.append(parent)
    if request.method == 'POST':    # academic coach adding to CRM
        date = request.POST['contact_date']
        msg = request.POST['contact_message']
        contact = Contact(student=student, date=date, message=msg)
        contact.save()

        # have to update the contacts
    contacts = Contact.objects.filter(student=student)
    no_contacts = (len(contacts) == 0)
    return render(request, 'student/profile.html', {'student': student, 'contacts': contacts, 'parents': parents,  'page': page,
                                                    'no_contacts': no_contacts, 'no_classes': no_classes, 'coach': coach})


def track_grades_view(request, username):
    page = 'grades'
    coach = is_coach(request)
    student = Student.objects.get(username=username)
    sessions = Session.objects.filter(student=student).order_by('date')
    if request.method == 'POST':
        date = request.POST['entry_date']
        for subject in student.class_set.all():
            score = request.POST[subject.name + '_score']
            session_number = str(int(request.POST['session_number']) + 1)

            grade_submission = ClassGrade(subject=subject, date=date, score=score, session_number=session_number)
            grade_submission.save()
    return render(request, 'student/track_grades.html', {'student': student, 'coach': coach, 'sessions': sessions, 'page': page})


def schedule_view(request, username):
    page = 'schedule'
    coach = is_coach(request)
    student = Student.objects.get(username=username)
    if request.method == 'POST':
        name = request.POST['class_name']
        if Class.objects.filter(name=name, student=student).exists():
            class_to_edit = Class.objects.get(name=name, student=student)
            class_to_edit.teacher = request.POST['new_teacher']
            class_to_edit.notes = request.POST['new_notes']
            class_to_edit.late_work_policy = request.POST['new_policy']
            class_to_edit.save()
        else:
            teacher = request.POST['class_teacher']
            notes = request.POST['class_notes']
            late_work_policy = request.POST['class_policy']
            new_class = Class(student=student, name=name, teacher=teacher, notes=notes, late_work_policy=late_work_policy)
            new_class.save()
    has_classes = len(student.class_set.all()) > 0
    return render(request, 'student/schedule.html', {'student': student, 'has_classes': has_classes, 'coach': coach, 'page': page})


def edit_class_view(request, username, class_id):
    coach = is_coach(request)
    class_object = Class.objects.get(id=class_id)
    class_object.name = request.POST['class_name']
    class_object.teacher = request.POST['new_teacher']
    class_object.notes = request.POST['new_notes']
    class_object.late_work_policy = request.POST['new_policy']
    class_object.save()
    return redirect('student/' + username + '/schedule')


def track_habits_redirect_view(request, username):
    student = Student.objects.get(username=username)
    sessions = Session.objects.filter(student=student).order_by('date')
    session_number = str(len(sessions))
    return redirect('student/' + username + '/track_habits/' + session_number)


def track_habits_view(request, username, session_number):
    page = 'habits'
    coach = is_coach(request)
    student = Student.objects.get(username=username)
    sessions = Session.objects.filter(student=student).order_by('date')
    index = 1
    session = None
    for option in sessions:
        if index == int(session_number):
            session = option
        index = index + 1
    if request.method == 'POST':
        habit_title = request.POST['habit_title']
        question = request.POST['rubric_question']
        answer = request.POST['rubric_answer']
        habit = Habit(student=student, title=habit_title, rubric_question=question, rubric_answer=answer)
        habit.save()
    return render(request, 'student/track_habits.html', {'student': student, 'coach': coach, 'sessions': sessions, 'session_number':
                                                         session_number, 'session': session,  'page': page})


def add_habit_score_view(request, username, session_number, habit_id):
    student = Student.objects.get(username=username)
    habit = Habit.objects.get(student=student, id=habit_id)
    if request.method == 'POST':
        score = request.POST['score']
        habit_score = HabitScore(habit=habit, date=date.today(), score=score, session_number=session_number)
        habit_score.save()
    return redirect('/student/' + username + '/track_habits/' + session_number)


def session_redirect_view(request, username):
    student = Student.objects.get(username=username)
    if Session.objects.filter(student=student).exists():
        number = len(Session.objects.filter(student=student))
        return redirect('/student/' + username + '/session/' + str(number))
    else:
        return redirect('/student/' + username + '/session/0')


def pre_session_view(request, username, session_number):
    page = 'session'
    coach = is_coach(request)
    student = Student.objects.get(username=username)
    if request.method == 'POST':
        date = request.POST['new_session_date']
        new_session = Session(student=student, date=date)
        new_session.save()
        new_session_number = str(len(Session.objects.filter(student=student)))
        return redirect('/student/' + username + '/session/' + new_session_number)
    active_session = True
    session = None
    if session_number == '0':
        active_session = False
    else:
        sessions = Session.objects.filter(student=student).order_by('date')
        index = 1
        for current_session in sessions:
            if index == int(session_number):
                session = current_session
            index = index + 1
    sessions = Session.objects.filter(student=student)
    return render(request, 'student/pre_session.html', {'student': student, 'session': session, 'active_session':
                                                        active_session, 'coach': coach, 'sessions': sessions, 'session_number':
                                                        session_number,  'page': page})


def save_session_view(request, username, session_id):
    student = Student.objects.get(username=username)
    session = Session.objects.get(student=student, id=session_id)
    if request.method == 'POST':
        session.celebrations = request.POST['celebrations']
        session.missing_work = request.POST['missing_work']
        session.questions_about_session = request.POST['questions']
        session.upcoming_due_dates = request.POST['due_dates']
        session.coach_follow_up = request.POST['follow_up']
        session.student_commitments = request.POST['commitments']
        session.notes = request.POST['notes']
        session.save()
    index = 1
    number = 0
    for comparison in Session.objects.filter(student=student).order_by('date'):
        if session.date == comparison.date:
            number = index
        else:
            index = index + 1
    return redirect('/student/' + student.username + '/session/' + str(number))


def analyze_sessions_view(request, username):
    page = 'session'
    coach = is_coach(request)
    student = Student.objects.get(username=username)
    sessions = Session.objects.filter(student=student).order_by('date')
    if request.method == 'POST':
        selected_sessions = []
        if request.POST.get('all_sessions', False):
            selected_sessions = sessions
        else:
            for session in sessions:
                if request.POST.get('session-' + str(session.id), False):
                    selected_sessions.append(session)
        return render(request, 'student/analyze_all_sessions.html', {'student': student, 'sessions': sessions,
                                                                     'selected': True, 'selected_sessions': selected_sessions,
                                                                     'all_categories_selected': request.POST.get('all_categories', False),
                                                                     'celebrations_selected': request.POST.get('celebrations', False),
                                                                     'missing_work_selected': request.POST.get('missing_work', False),
                                                                     'questions_selected': request.POST.get('questions', False),
                                                                     'due_dates_selected': request.POST.get('due_dates', False),
                                                                     'follow_up_selected': request.POST.get('follow_up', False),
                                                                     'commitments_selected': request.POST.get('commitments', False),
                                                                     'notes_selected': request.POST.get('notes', False) , 'coach': coach,
                                                                     'page': page})

    return render(request, 'student/analyze_all_sessions.html', {'student': student, 'sessions': sessions, 'selected': True,
                                                                 'all_categories_selected': True, 'selected_sessions': sessions,
                                                                 'celebrations_selected': False, 'coach': coach,  'page': page})


def progress_visualization_view(request, username):
    page = 'visualize'
    coach = is_coach(request)
    student = Student.objects.get(username=username)
    metric_list = []
    session_range = []
    session_count = len(student.session_set.all()) + 1
    current_session = 1
    the_sessions = Session.objects.filter(student=student).order_by('date')
    for the_session in the_sessions:
        session_string = 'Session ' + str(current_session)
        session_range.append(session_string)
        current_session = current_session + 1
    for subject in student.class_set.all():
        data = []
        current_session_number = 1
        while current_session_number <= session_count:
            if subject.classgrade_set.filter(session_number=current_session_number).exists():
                most_recent = subject.classgrade_set.filter(session_number=current_session_number).order_by('date').last()
                data.append(most_recent.score)
            else:
                data.append(None)
            current_session_number = current_session_number + 1
        metric_list.append({'metric_name': subject.name, 'data': data})
    for habit in student.habit_set.all():
        data = []
        current_session_number = 1
        while current_session_number <= session_count:
            if habit.habitscore_set.filter(session_number=current_session_number).exists():
                most_recent = habit.habitscore_set.filter(session_number=current_session_number).order_by('date').last()
                data.append(most_recent.score*10)
            else:
                data.append(None)
            current_session_number = current_session_number + 1
        metric_list.append({'metric_name': habit.title, 'data': data})
    return render(request, 'student/visualizations.html', {'student': student, 'coach': coach, 'metric_list': metric_list,
                                                           'session_range': session_range, 'page': page})


def delete_student_view(request, username):
    if request.method == 'POST':
        coach = is_coach(request)
        if coach:
            academic_coach = AcademicCoach.objects.get(username=request.user.username)
            student = Student.objects.get(username=username)
            if student.academic_coach.id == academic_coach.id:
                student.delete()
    return redirect('/coach/home')
