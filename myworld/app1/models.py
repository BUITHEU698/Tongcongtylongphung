import email
from pyexpat import model
from django.db import models
from matplotlib.style import use


#--------------contact-------------
class contactModel(models.Model):
    username = models.CharField(max_length= 25)
    email = models.EmailField()
    subject = models.CharField(max_length= 100)
    message = models.TextField()
