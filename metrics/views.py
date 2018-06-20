from django.shortcuts import render
from student.models import Student, Teacher
from .models import Metric, Score


def quick_log(request):
    if request.method == 'POST':
        teacher = None
        na = False
        hw = None
        student = Student.objects.get(name='Max')
        which_teacher = request.POST['teacher']
        if which_teacher == 'teacher1':
            teacher = Teacher.objects.get(name='Michael Chellman')
        elif which_teacher == 'teacher2':
            teacher = Teacher.objects.get(name='Chelsea Henry')
        elif which_teacher == 'teacher3':
            teacher = Teacher.objects.get(name='Claire Holman')
        elif which_teacher == 'teacher4':
            teacher = Teacher.objects.get(name='Lele Horich')
        date = request.POST['date']
        if request.POST.get('attentive', False):
            attentive_score = 1
        else:
            attentive_score = 0
        if request.POST.get('organized', False):
            organized = 1
        else:
            organized = 0
        if request.POST.get('well-behaved', False):
            behaved = 1
        else:
            behaved = 0
        homework_raw = request.POST['hw']
        if homework_raw == 'na':
            hw = 0
            na = True
        elif homework_raw == 'no':
            hw = 0
        elif homework_raw == 'yes':
            hw = 1

        attentive_metric = Metric.objects.get(name__icontains='Attentive', student=student)
        score1 = Score(metric=attentive_metric, teacher=teacher, score=attentive_score, date=date)
        score1.save()

        organized_metric = Metric.objects.get(name='Organization', student=student)
        score2 = Score(metric=organized_metric, teacher=teacher, score=organized, date=date)
        score2.save()

        behaved_metric = Metric.objects.get(name='Well behaved', student=student)
        score3 = Score(metric=behaved_metric, teacher=teacher, score=behaved, date=date)
        score3.save()

        hw_metric = Metric.objects.get(name='HW Complete', student=student)
        score4 = Score(metric=hw_metric, teacher=teacher, score=hw, date=date, NA=na)
        score4.save()
        return render(request, 'quick_log.html', {'teacher': teacher, 'attentive': attentive_score, 'organized': organized, 'behaved': behaved, 'hw': hw, 'success': True})
    return render(request, 'quick_log.html', context=None)


def view_scores(request):
    student = Student.objects.get(name='Max')
    attentive_metric = Metric.objects.get(student=student, name='Attentive')
    organized_metric = Metric.objects.get(student=student, name='Organization')
    behaved_metric = Metric.objects.get(student=student, name='Well behaved')
    hw_metric = Metric.objects.get(student=student, name='HW Complete')
    attentive = Score.objects.filter(metric=attentive_metric)
    organized = Score.objects.filter(metric=organized_metric)
    well_behaved = Score.objects.filter(metric=behaved_metric)
    hw = Score.objects.filter(metric=hw_metric)
    reports = [attentive, organized, well_behaved, hw]
    return render(request, 'view_scores.html', {'reports': reports})
