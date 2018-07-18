from django.shortcuts import render, redirect
from student.models import AcademicCoach, Student, School, Parent, Contact
from datetime import date
from Vana18.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail


def start_view(request):
    if request.user.is_active:
        if request.user.username == 'marni' or request.user.username == 'Test':
            return redirect('/coach/home')
        else:
            return redirect('/student/' + request.user.username + '/profile')
    else:
        return redirect('/login')


def setup_view(request):
    ready = True
    if ready:
        coach = AcademicCoach(name='Test', username='Test', email='asdg@fake.asd', phone_number='1')
        coach.save()
        return redirect('/coach/home')
    else:
        return redirect('/coach/home')


def all_student_view(request):
    if request.user.username != 'marni':
        return redirect('/student/' + request.user.username + '/profile')
    academic_coach = AcademicCoach.objects.get(username='marni')
    names = []
    for student in Student.objects.filter(academic_coach=academic_coach):
        names.append((student.name, student.username))
    return render(request, 'coach/homepage.html', {'students': names, 'student': None})


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
        subject = "Invitation from " + academic_coach.name + ' to join Vana Learning'
        message = new_student.name + ',\n\n' + academic_coach.name + ' has invited you to make an account on Vana Learning. ' \
                                                                     'Your username is ' + new_student.username + '.\n\nPlease create your account' \
                                                                                                               'by following this link: https://vana18.herokuapp.com/signup/' + new_student.username + '\n\nBest,\nThe Vana Learning Team'
        sender_email = 'jstafford@vanalearning.com'
        recipient_email = new_student.email
        send_mail(subject, message, sender_email, [recipient_email])
    return render(request, 'coach/add_student.html', context=None)


def create_student_account_view(request, username):
    if Student.objects.filter(username=username).exists():
        student = Student.objects.get(username=username)
    else:
        return redirect("https://www.vana-learning.com")
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        birthday = request.POST['birthday']
        grades_link = request.POST['grades_link']
        if grades_link[0:7] != 'https//' and grades_link[0:6] != 'http//':
            grades_link = 'https://' + grades_link
        zoom_link = request.POST['zoom_link']
        if zoom_link[0:7] != 'https//' and zoom_link[0:6] != 'http//':
            zoom_link = 'https://' + zoom_link
        school_name = request.POST['school_name']
        school_website = request.POST['school_website']
        if school_website[0:7] != 'https//' and school_website[0:6] != 'http//':
            school_website = 'https://' + school_website
        school_calendar = request.POST['school_calendar']
        if school_calendar[0:7] != 'https//' and school_calendar[0:6] != 'http//':
            school_calendar = 'https://' + school_calendar
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
        student.birthday = birthday
        student.zoom_link = zoom_link
        student.grades_link = grades_link
        student.school = school
        student.save()
        return redirect('/student/' + student.username + '/profile')
    return render(request, 'coach/create_student_account.html', {'student': student})


def signup_view(request, username):
    if Student.objects.filter(username=username).exists():
        student = Student.objects.get(username=username)
        if User.objects.filter(username=username).exists():
            return redirect('/' + student.academic_coach.username + '/new_student/' + student.username)
    else:
        return redirect('https://www.vana-learning.com')
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return redirect('/' + student.academic_coach.username + '/new_student/' + student.username)
        else:
            form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form, 'student': student})
