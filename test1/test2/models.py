from pyexpat import model
from time import time
from turtle import mode
from venv import create
from django.db import models

# Create your models here.
class question (models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField()

class choice (models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    void = models.IntegerField(default=0)


