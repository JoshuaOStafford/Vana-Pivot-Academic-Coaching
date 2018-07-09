from student.models import Student, AcademicCoach, School, Parent, Contact, Class


def student_has_no_classes(request):
    if request.user.is_active:
        if Student.objects.filter(username=request.user.username):
            student = Student.objects.get(username=request.user.username)
            if len(student.class_set.all()) == 0:
                return True
    else:
        return False

