
from django.urls import path
from .import views
app_name = 'app1'

urlpatterns = [
    path('', views.index, name="index"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('contact', views.contact, name="contact"),
    # path('getContact', views.getContact, name="getContact"),
    path('detail', views.detail, name="detail"),
    path('shop', views.shop, name="shop"),
    path('detail', views.detail, name="detail"),
]
