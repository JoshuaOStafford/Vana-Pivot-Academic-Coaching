from django.shortcuts import render, redirect
from student.models import AcademicCoach, Student, School, Parent, Contact
from datetime import date


def setup_view(request):
    ready = True
    if ready:
        # insert setup code here
        return redirect('/marni/home')
    else:
        return redirect('/marni/home')


def all_student_view(request):
    nav_bar_hidden = True
    academic_coach = AcademicCoach.objects.get(username='marni')
    names = []
    for student in Student.objects.filter(academic_coach=academic_coach):
        names.append((student.name, student.username))
    return render(request, 'coach/homepage.html', {'students': names, 'nav_bar_hidden': nav_bar_hidden})


def add_student_view(request):
    academic_coach = AcademicCoach.objects.get(username='marni')
    if request.method == 'POST':
        student_name = request.POST['name']
        student_username = request.POST['username']
        student_email = request.POST['email']
        new_student = Student(name=student_name, username=student_username, academic_coach=academic_coach,
                              birthday=date.today(), school=School.objects.get(name='No School Entered'),
                              email=student_email)
        new_student.save()
        # copy over code to email a student
    return render(request, 'coach/add_student.html', context=None)


def create_student_account_view(request, username):
    if Student.objects.filter(username=username).exists():
        student = Student.objects.get(username=username)
    else:
        return redirect("https://www.vana-learning.com")
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        # birthday = request.POST['birthday']
        grades_link = request.POST['grades_link']
        zoom_link = request.POST['zoom_link']

        school_name = request.POST['school_name']
        school_website = request.POST['school_website']
        school_calendar = request.POST['school_calendar']

        school = School(name=school_name, website_link=school_website, calendar_link=school_calendar)
        school.save()

        parent1_name = request.POST['parent1_name']
        parent1_phone = request.POST['parent1_phone']
        parent1_email = request.POST['parent1_email']
        parent1 = Parent(student=student, name=parent1_name, email=parent1_email, phone_number=parent1_phone)
        parent1.save()
        if request.POST.get('parent2_name', False) and request.POST.get('parent2_name', False) and \
                request.POST.get('parent2_name', False):
            parent2_name = request.POST['parent2_name']
            parent2_phone = request.POST['parent2_phone']
            parent2_email = request.POST['parent2_email']
            parent2 = Parent(student=student, name=parent2_name, email=parent2_email, phone_number=parent2_phone)
            parent2.save()
        student.phone_number = phone_number
        # student.birthday = birthday
        student.zoom_link = zoom_link
        student.grades_link = grades_link
        student.school = school
        student.save()

    return render(request, 'coach/create_student_account.html', {'student': student})