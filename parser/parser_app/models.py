from django.db import models
from django.contrib.auth.models import User

# from django.contrib.auth.models import User

# Create your models here.
class ChildQuestions(models.Model):
    question = models.CharField(max_length=200)


class Question(models.Model):
    question_text = models.TextField()


class Test(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tests")
    title = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question, related_name="tests")


class Answer(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
