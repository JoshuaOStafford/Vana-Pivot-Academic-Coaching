from student.models import Student, AcademicCoach, School, Parent, Contact, Class


def student_has_no_classes(request):
    if request.user.is_active:
        if Student.objects.filter(username=request.user.username):
            student = Student.objects.get(username=request.user.username)
            if len(student.class_set.all()) == 0:
                return True
    else:
        return False


def is_coach(request):
    if request.user.is_active:
        if AcademicCoach.objects.filter(username=request.user.username).exists():
            return True
    else:
        return False


def recover_password(student):
    message = '''{name}, 

Your security code is {security_code}. Please reset your password at https://www.vanalearning.com/student/forgot-password/{username}

Best,
The Vana Learning Team
'''.format(name=student.name, security_code=student.code, username=student.username)
    return message
