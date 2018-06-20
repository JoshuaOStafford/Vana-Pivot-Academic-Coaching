from django.db import models
from core.models import TimeStampedModel
from student.models import Student, Teacher
from django.utils import timezone


class Metric(TimeStampedModel):
    name = models.CharField(max_length=50)
    max_score = models.PositiveIntegerField(default=10)
    student = models.ForeignKey(Student)


class Score(TimeStampedModel):
    metric = models.ForeignKey(Metric)
    teacher = models.ForeignKey(Teacher)
    time = models.PositiveIntegerField(default=4)
    score = models.PositiveIntegerField()
    date = models.DateField(default=timezone.now)
    NA = models.BooleanField(default=False)