from django.shortcuts import render, redirect
from student.models import AcademicCoach, Student, School, Parent
from datetime import date


def setup_view(request):
    already_setup = False
    if already_setup:
        return redirect('/marni/home')
    else:
        marni = AcademicCoach(name='Marni Pasch', username='marni', state='Florida', email='joshua.o.stafford@vanderbilt.edu', phone_number='225-304-2611')
        marni.save()
        bullis = School(name='Bullis School', calendar_link='https://www.bullis.org/page.cfm?p=845',
                        website_link='https://www.bullis.org/page.cfm?p=1', state='Maryland')
        bullis.save()
        rob_bday = date(1995, 8, 12)
        rob = Student(name='Rob Trone', username='robtrone', academic_coach=marni, phone_number='301-704-7703',
                      email='robert.j.trone@vanderbilt.edu', zoom_link='https://zoom.us/j/570189575',
                      grades_link='https://www.powerschool.com/', birthday=rob_bday, school=bullis)
        rob.save()
        return redirect('/marni/home')


def all_student_view(request):
    academic_coach = AcademicCoach.objects.get(username='marni')
    names = []
    for student in Student.objects.filter(academic_coach=academic_coach):
        names.append(student.name)
    return render(request, 'coach/homepage.html', {'students': names, 'hidden': False})
