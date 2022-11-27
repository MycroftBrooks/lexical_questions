from django.db import models
# Create your models here.
class ChildQuestions(models.Model):
    question = models.CharField(max_length=200) 
