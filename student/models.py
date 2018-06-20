from django.db import models
from core.models import TimeStampedModel


class Teacher(TimeStampedModel):
    name = models.CharField(max_length=50)


class Student(TimeStampedModel):
    name = models.CharField(max_length=50)
    two_parents = models.BooleanField(default=False)
    parent1_name = models.CharField(max_length=50)
    parent2_name = models.CharField(max_length=50)
    birthday = models.DateField(default='01/01/2000')
    student_phone = models.CharField(max_length=20)
    parent1_phone = models.CharField(max_length=20)
    parent2_phone = models.CharField(max_length=20)
    parent1_email = models.EmailField()
    parent2_email = models.EmailField()
    student_email = models.EmailField()
    school_name = models.CharField(max_length=50)
    school_website = models.URLField()
    school_calendar = models.URLField()
    grades_account = models.URLField()
    teachers = models.ManyToManyField(Teacher)


class Class(TimeStampedModel):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    notes = models.CharField(max_length=1000)
    late_work_policy = models.CharField(max_length=1000)


class Contacted(TimeStampedModel):
    note = models.CharField(max_length=500)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)



