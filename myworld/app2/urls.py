from django.urls import path
from .import views
app_name = 'app2'

urlpatterns = [
    path('login', views.login, name="login"),
    path('signup', views.member.as_view(), name="signup"),
    path('login', views.loginUser.as_view(), name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('order', views.order.as_view(), name="order"),
]

