from django.shortcuts import render
from student.models import Student, AcademicCoach, School, Parent, Contact, Class
from student.helpers import student_has_no_classes


def profile_view(request, username):
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
                                                    'no_contacts': no_contacts, 'no_classes': no_classes})


def track_grades_view(request, username):
    student = Student.objects.get(username=username)
    return render(request, 'student/track_grades.html', {'student': student})


def schedule_view(request, username):
    student = Student.objects.get(username=username)
    if request.method == 'POST':
        name = request.POST['class_name']
        teacher = request.POST['class_teacher']
        notes = request.POST['class_notes']
        late_work_policy = request.POST['class_policy']
        new_class = Class(student=student, name=name, teacher=teacher, notes=notes, late_work_policy=late_work_policy)
        new_class.save()
    has_classes = len(student.class_set.all()) > 0
    return render(request, 'student/schedule.html', {'student': student, 'has_classes': has_classes})


def track_habits_view(request):
    return render(request, 'student/track_habits.html', context=None)


def pre_session_view(request):
    return render(request, 'student/pre_session.html', context=None)


def progress_visualization_view(request):
    return render(request, 'student/visualizations.html', context=None)