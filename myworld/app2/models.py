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
        ('1', 'Ẩn'),
        ('2', 'Hiện'),
    ]
    portfolioName = models.CharField('Tên danh sách',max_length=200, blank= False, null = False)
    portfolioBody = models.TextField('Mô tả danh sách')
    portfolioPub = models.CharField('Hiển thị',
        max_length=250,  default="2", choices=CHOICES)
    portfolioTimePub = models.DateTimeField('Thời gian hiển thị', default=timezone.now)
    portfolioImg = models.FileField('Ảnh minh họa')
    
    def __str__(self):
        return self.portfolioName
 


