from django.shortcuts import render, redirect
from student.models import Student, AcademicCoach, School, Parent, Contact, Class, ClassGrade, Habit, HabitScore, Session
from student.helpers import student_has_no_classes, is_coach
from datetime import date, timedelta


def profile_view(request, username):
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
    return render(request, 'student/profile.html', {'student': student, 'contacts': contacts, 'parents': parents,
                                                    'no_contacts': no_contacts, 'no_classes': no_classes, 'coach': coach})


def track_grades_view(request, username):
    coach = is_coach(request)
    student = Student.objects.get(username=username)
    if request.method == 'POST':
        date = request.POST['entry_date']
        for subject in student.class_set.all():
            score = request.POST[subject.name + '_score']
            grade_submission = ClassGrade(subject=subject, date=date, score=score)
            grade_submission.save()
    return render(request, 'student/track_grades.html', {'student': student, 'coach': coach})


def schedule_view(request, username):
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
    return render(request, 'student/schedule.html', {'student': student, 'has_classes': has_classes, 'coach': coach})


def edit_class_view(request, username, class_id):
    coach = is_coach(request)
    class_object = Class.objects.get(id=class_id)
    class_object.name = request.POST['class_name']
    class_object.teacher = request.POST['new_teacher']
    class_object.notes = request.POST['new_notes']
    class_object.late_work_policy = request.POST['new_policy']
    class_object.save()
    return redirect('student/' + username + '/schedule')


def track_habits_view(request, username):
    coach = is_coach(request)
    student = Student.objects.get(username=username)
    if request.method == 'POST':
        habit_title = request.POST['habit_title']
        question = request.POST['rubric_question']
        answer = request.POST['rubric_answer']
        habit = Habit(student=student, title=habit_title, rubric_question=question, rubric_answer=answer)
        habit.save()
    return render(request, 'student/track_habits.html', {'student': student, 'coach': coach})


def add_habit_score_view(request, username, habit_id):
    student = Student.objects.get(username=username)
    habit = Habit.objects.get(student=student, id=habit_id)
    if request.method == 'POST':
        score = request.POST['score']
        if HabitScore.objects.filter(habit=habit, date=date.today()).exists():  # only possible to have one score daily
            habit_score = HabitScore.objects.get(habit=habit, date=date.today())
            habit_score.score = score
        else:
            habit_score = HabitScore(habit=habit, date=date.today(), score=score)
        habit_score.save()
    return redirect('/student/' + username + '/track_habits')


def pre_session_view(request, username):
    coach = is_coach(request)
    student = Student.objects.get(username=username)
    if request.method == 'POST':
        date = request.POST['new_session_date']
        new_session = Session(student=student, date=date)
        new_session.save()
    active_session = False
    session = None
    if Session.objects.filter(student=student).order_by('date').exists():
        session = Session.objects.filter(student=student).order_by('date').last()
        active_session = True
    return render(request, 'student/pre_session.html', {'student': student, 'session': session, 'active_session':
                                                        active_session, 'coach': coach})


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
    return redirect('/student/' + student.username + '/session')


def analyze_sessions_view(request, username):
    coach = is_coach(request)
    student = Student.objects.get(username=username)
    sessions = Session.objects.filter(student=student).order_by('date')
    if request.method == 'POST':
        selected_sessions = []
        if request.POST['all_sessions']:
            selected_sessions = sessions
        else:
            for session in sessions:
                if request.POST['session-' + session.id]:
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
                                                                     'notes_selected': request.POST.get('notes', False) , 'coach': coach})

    return render(request, 'student/analyze_all_sessions.html', {'student': student, 'sessions': sessions, 'selected': True,
                                                                 'all_categories_selected': True, 'selected_sessions': sessions,
                                                                 'celebrations_selected': False, 'coach': coach})


def progress_visualization_view(request, username):
    coach = is_coach(request)
    student = Student.objects.get(username=username)
    last_date = date(year=2017, day=1, month=1)
    first_date = date(year=2020, day=31, month=12)
    metric_list = []
    for subject in student.class_set.all():
        current_set = subject.classgrade_set.all().order_by('date')
        if current_set.first().date < first_date:
            first_date = current_set.first().date
        if current_set.last().date > last_date:
            last_date = current_set.last().date
    date_range = []
    while first_date <= last_date:
        date_range.append(first_date)
        first_date = first_date + timedelta(days=1)

    for subject in student.class_set.all():
        data = []
        for possible_score_date in date_range:
            if subject.classgrade_set.filter(date=possible_score_date).exists():
                data.append(subject.classgrade_set.get(date=possible_score_date).score)
            else:
                data.append(None)
        metric_list.append({'subject': subject, 'data': data})
    return render(request, 'student/visualizations.html', {'student': student, 'coach': coach, 'metric_list': metric_list,
                                                           'date_range': date_range})