from django.db import models
import email
from pyexpat import model
from django.db import models
from django.urls import reverse
from matplotlib.style import use

# Create your models here.


FRUIT_CHOICES = [
    ('1', 'Ẩn'),
    ('2', 'Hiện'),
]

class PortfolioModel(models.Model):
    portfolioName = models.CharField(max_length=200)
    portfolioBody = models.TextField()
    portfolioPub = models.CharField(
        label='Hiển Thị', widget=models.RadioSelect(choices=FRUIT_CHOICES))
    portfolioTimePub = models.DateTimeField()
    portfolioImg = models.FileField()
    def __str__(self):
        return self.portfolioName
 


