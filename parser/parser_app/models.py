from django.db import models
from django.contrib.auth.models import User


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


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    right_answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)
