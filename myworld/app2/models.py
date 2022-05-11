from django.db import models
import email
from pyexpat import model
from django.db import models
from django.urls import reverse
from matplotlib.style import use

# Create your models here.




class PortfolioModel(models.Model):
    CHOICES = [
        ('1', 'Ẩn'),
        ('2', 'Hiện'),
    ]
    portfolioName = models.CharField(max_length=200)
    portfolioBody = models.TextField()
    portfolioPub = models.CharField(
        max_length=250,  default="1", choices=CHOICES)
    portfolioTimePub = models.DateTimeField()
    portfolioImg = models.FileField()
    
    def __str__(self):
        return self.portfolioName
 


