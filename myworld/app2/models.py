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
    portfolioBody = models.TextField('Mô tả danh sách',blank= False, null = False)
    portfolioPub = models.CharField('Hiển thị', max_length=250,  default="1", choices=CHOICES, blank= False, null = False)
    portfolioTimePub = models.DateTimeField('Thời gian hiển thị', blank= False, null = False )
    portfolioImg = models.FileField()
    
    def __str__(self):
        return self.portfolioName



class ProductsModel(models.Model):
    CHOICES = [
        ('1', 'Hiển Thị'),
        ('2', 'Ẩn'),
    ]
    productsName = models.CharField('Tên sản phẩm',max_length=200, blank= False, null = False)
    productsBody = models.TextField('Mô tả sản phẩm',blank= False, null = False)
    productsImg = models.FileField('Ảnh sản phẩm')
    productsPrice = models.FloatField('Giá bán', default= 0)
    productsPriceOther = models.FloatField('Giá so sánh', default= 0)
    inventory = models.FloatField('Hàng tồn kho', default= 0)
    productsPub = models.CharField('Hiển thị', max_length=250,  default="1", choices=CHOICES, blank= False, null = False)
    productsTimePub = models.DateTimeField('Thời gian hiển thị', blank= False, null = False )
    portfolioModel = models.ForeignKey(PortfolioModel, on_delete= models.CASCADE)
    weight = models.FloatField('Khối lượng sản phẩm', default= 0)
    def __str__(self):
        return self.productsName