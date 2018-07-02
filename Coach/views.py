from django.shortcuts import render, redirect
from student.models import AcademicCoach, Student, School, Parent
from datetime import date


def setup_view(request):
    already_setup = False
    if already_setup:
        return redirect('/marni/home')
    else:
        return redirect('/marni/home')


def all_student_view(request):
    academic_coach = AcademicCoach.objects.get(username='marni')
    names = []
    for student in Student.objects.filter(academic_coach=academic_coach):
        names.append((student.name, student.username))
    return render(request, 'coach/homepage.html', {'students': names, 'hidden': False})
