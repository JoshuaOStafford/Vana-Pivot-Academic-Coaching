from django.db import models
from core.models import TimeStampedModel
from django.core.validators import URLValidator
from django.utils import timezone


class AcademicCoach(TimeStampedModel):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=16)
    state = models.CharField(max_length=20, default='Unknown')
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)


class School(TimeStampedModel):
    name = models.CharField(max_length=60)
    calendar_link = models.TextField(validators=[URLValidator()])
    website_link = models.TextField(validators=[URLValidator()])
    state = models.CharField(max_length=20, default='Unknown')


class Student(TimeStampedModel):
    username = models.CharField(max_length=16)
    academic_coach = models.ForeignKey(AcademicCoach, on_delete=models.CASCADE, default=None)
    # basic info
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    zoom_link = models.TextField(validators=[URLValidator()])
    grades_link = models.TextField(validators=[URLValidator()])
    birthday = models.DateField(default=timezone.now)   # without default, would get error when making student account
    # will have parents through Foreign Key
    school = models.ForeignKey(School, on_delete=models.PROTECT, default=None)


class Parent(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=16)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()


class Session(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    celebrations = models.TextField()
    missing_work = models.TextField()
    questions_about_session = models.TextField()
    upcoming_due_dates = models.TextField()
    coach_follow_up = models.TextField()
    student_commitments = models.TextField()
    notes = models.TextField()


class Contact(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    message = models.TextField()


class Habit(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    rubric_question = models.TextField()
    rubric_answer = models.TextField()
    max_score = models.PositiveIntegerField(default=10)


class HabitScore(TimeStampedModel):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    score = models.PositiveIntegerField()


class Class(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    teacher = models.CharField(max_length=30)
    notes = models.TextField()
    late_work_policy = models.TextField()
    max_score = models.PositiveIntegerField(default=100)


class ClassGrade(TimeStampedModel):
    subject = models.ForeignKey(Class, on_delete=models.CASCADE)  # had to call it subject since class is keyword
    date = models.DateField(default=timezone.now)
    score = models.PositiveIntegerField()






