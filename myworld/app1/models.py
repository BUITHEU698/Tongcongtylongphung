
import email
from pyexpat import model
from venv import create
from django.db import models
from django.urls import reverse
from matplotlib.style import use
from numpy import quantile
from app2.models import ProductsModel
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# --------------contact-------------
class contactModel(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email

# --------------postBlog-------------
class postBlog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail',args=[self.id,])
    
class UserModel (models.Model):
    userName = models.CharField('LastName',default='Name',  max_length=25)
    email = models.EmailField( 'Email',default='')
    phoneNumber = models.CharField('Số điện thoại', default= 0, max_length= 11)
    password = models.CharField('password', default='',max_length=30)
    resetpassword = models.CharField('resetpassword',default='', max_length=30)

class CartModel (models.Model):
    user = models.ForeignKey(UserModel, on_delete= models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class CartItemModel (models.Model):
    cart = models.ForeignKey(CartModel, on_delete= models.CASCADE)
    products = models.ForeignKey(ProductsModel, on_delete= models.CASCADE)
    quantile = models.IntegerField('Số lượng', default=0)



class OrderModel (models.Model):
    user = models.ForeignKey(UserModel, on_delete= models.CASCADE)
    cart = models.ForeignKey(CartModel, on_delete= models.CASCADE)
    ShipAddress = models.CharField('Địa chỉ ship', max_length= 255)
    order_description = models.TextField(default='')
    completed = models.BooleanField(default= False)