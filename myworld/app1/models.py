import email
from pyexpat import model
from django.db import models
from matplotlib.style import use

# Create your models here.
class contacForm(models.Model):
    usename = models.CharField(max_length= 25)
    email = models.EmailField()
    body = models.TextField()