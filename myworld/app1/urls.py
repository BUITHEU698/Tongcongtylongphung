
from django.urls import path
from .import views
app_name = 'app1'

urlpatterns = [
    path('', views.index, name="index"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('contact', views.contact.as_view(), name="contact"),
    path('detail', views.detail, name="detail"),
    path('shop', views.shop, name="shop"),
    path('detail', views.detail, name="detail"),
    path('blog', views.blog, name="blog"),
    path('blog1', views.blog1, name="blog1"),
    path('blog2', views.blog2, name="blog2"),
]
