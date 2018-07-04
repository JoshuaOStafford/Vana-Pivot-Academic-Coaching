from django.shortcuts import render, redirect
from student.models import AcademicCoach, Student, School, Parent
from datetime import date


def setup_view(request):
    ready = True
    if ready:
        rob = Student.objects.get(username='robtrone')
        rob_dad = Parent(student=rob, name='David Trone', username='davidtrone',
                         email='david.trone@gmail.com', phone_number='301-521-6146')
        rob_dad.save()
        return redirect('/marni/home')
    else:
        return redirect('/marni/home')


def all_student_view(request):
    academic_coach = AcademicCoach.objects.get(username='marni')
    names = []
    for student in Student.objects.filter(academic_coach=academic_coach):
        names.append((student.name, student.username))
    return render(request, 'coach/homepage.html', {'students': names, 'hidden': False})


def add_student_view(request):
    academic_coach = AcademicCoach.objects.get(username='marni')
    if request.method == 'POST':
        student_name = request.POST['student_name']
        student_username = request.POST['student_username']
        student_email = request.POST['student_email']
        new_student = Student(name=student_name, username=student_username, academic_coach=academic_coach,
                              birthday=date.today(), school=None, email=student_email)
        new_student.save()
        # copy over code to email a student
    return render(request, 'coach/add_student.html', context=None)


def create_student_account_view(request):
    # complete the students account information
    return render(request, 'coach/create_student_account.html', context=None)