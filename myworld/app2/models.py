from django.utils import timezone
from django.db import models
import email
from pyexpat import model
from django.db import models
from django.urls import reverse
from matplotlib.style import use

# Create your models here.




class PortfolioModel(models.Model):
    CHOICES = [
        ('1', 'Hiển Thị'),
        ('2', 'Ẩn'),
    ]
    portfolioName = models.CharField('Tên danh sách',max_length=200, blank= False, null = False)
    # portfolioBody = models.TextField('Mô tả danh sách',blank= False, null = False)
    # portfolioPub = models.CharField('Hiển thị', max_length=250,  default="1", choices=CHOICES, blank= False, null = False)
    # portfolioTimePub = models.DateTimeField('Thời gian hiển thị', blank= False, null = False)
    # portfolioImg = models.FileField()
    
    def __str__(self):
        return self.portfolioName
 


