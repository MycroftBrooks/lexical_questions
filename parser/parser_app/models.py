from django.db import models
from django.contrib.auth.models import User, Group


ANSWER_CHOICES = (
    ("a", "a"),
    ("b", "b"),
    ("c", "c"),
    ("d", "d"),
)


class ChildQuestions(models.Model):
    question = models.CharField(max_length=200)


class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    students = models.ManyToManyField(User, related_name="students", blank=True)


class Question(models.Model):
    test = models.ForeignKey(Test, related_name="questions", on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    right_answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)


class Bookpdf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to="pdfs/")
    students = models.ManyToManyField(User, related_name="studentsBook", blank=True)
