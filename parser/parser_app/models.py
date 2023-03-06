from django.db import models
from django.contrib.auth.models import User

# from django.contrib.auth.models import User

# Create your models here.
class ChildQuestions(models.Model):
    question = models.CharField(max_length=200)


class Test(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    time_limit = models.IntegerField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)


class Question(models.Model):
    TEXT_QUESTION = "text"
    MULTIPLE_CHOICE_QUESTION = "multiple_choice"
    ESSAY_QUESTION = "essay"
    QUESTION_TYPES = [
        (TEXT_QUESTION, "Text question"),
        (MULTIPLE_CHOICE_QUESTION, "Multiple choice question"),
        (ESSAY_QUESTION, "Essay question"),
    ]
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)


class Answer(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
