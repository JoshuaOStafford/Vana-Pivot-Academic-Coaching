from django.shortcuts import render
from student.models import Student, AcademicCoach, School, Parent, Contact


def profile_view(request, username):
    student = Student.objects.get(username=username)
    parents = []
    for parent in student.parent_set.all():
        parents.append(parent)
    contacts = Contact.objects.filter(student=student)
    no_contacts = (len(contacts) == 0)

    # still need to add form of some sort.
    if request.method == 'POST':    # academic coach adding to CRM
        date = request.POST['date']
        msg = request.POST['msg']
        contact = Contact(student=student, date=date, message=msg)
        contact.save()
    return render(request, 'student/profile.html', {'student': student, 'contacts': contacts, 'parents': parents,
                                                    'no_contacts': no_contacts})


def track_grades_view(request):
    amhistgrade = [45, 53, 60, 72, 84]
    chemgrade = [53, 62, 67, 64, 70]
    engrade = [83, 83, 86, 85, 88]
    frengrade = [73, 74, 83, 81, 80]
    hopegrade = [84, 83, 85, 88, 91]
    calcgrade = [67, 71, 73, 76, 77]
    dramgrade = [71, 69, 65, 70, 73]
    irgrade = [74, 78, 81, 83, 83]
    return render(request, 'student/track_grades.html', {'amhistgrade': amhistgrade, 'chemgrade': chemgrade,
                                                         'engrade': engrade, 'frengrade': frengrade,
                                                         'hopegrade': hopegrade, 'calcgrade': calcgrade,
                                                         'dramgrade': dramgrade, 'irgrade': irgrade})


def schedule_view(request):
    return render(request, 'student/schedule.html', context=None)


def track_habits_view(request):
    return render(request, 'student/track_habits.html', context=None)


def pre_session_view(request):
    return render(request, 'student/pre_session.html', context=None)


def progress_visualization_view(request):
    return render(request, 'student/visualizations.html', context=None)