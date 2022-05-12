
from django.urls import path
from .import views
app_name = 'app1'

urlpatterns = [
    path('', views.index.as_view(), name="index"),
    path('sitemap', views.sitemap, name="sitemap"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('contact', views.contact.as_view(), name="contact"),
    path('detail', views.detail, name="detail"),
    path('shop', views.shop.as_view(), name="shop"),
    path('detail', views.detail, name="detail"),
    path('blog', views.blog, name="blog"),
    path('<int:id>', views.blogDetail, name="blogDetail"),
    path('blog1', views.blog1, name="blog1"),
    path('blog2', views.blog2, name="blog2"),
    path('blog3', views.blog3, name="blog3"),
    path('blog4', views.blog4, name="blog4"),
    path('userLogin', views.userLogin.as_view(), name="userLogin"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.order.as_view(), name="register"),
    path('forgetPass', views.forgetPass, name="forgetPass"),
 

    # path('signup', views.member.as_view(), name="signup"),
    # path('login', views.loginUser.as_view(), name="login"),
    # path('logout', views.logoutUser, name="logout"),
    # path('order', views.order.as_view(), name="order"),
]
