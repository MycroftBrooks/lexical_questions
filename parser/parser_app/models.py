from django.db import models
from django.contrib.auth.models import User

# from django.contrib.auth.models import User

# Create your models here.
class ChildQuestions(models.Model):
    question = models.CharField(max_length=200)
