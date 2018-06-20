from django.shortcuts import render


def all_student_view(request):
    names = ['Adam', 'Beau', 'Emma', 'Mike','Nicole', 'Steven', 'Tommy']
    return render(request, 'coach/homepage.html', {'students': names, 'hidden': False})
