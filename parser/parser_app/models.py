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


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)

    def __str__(self):
        return self.question
