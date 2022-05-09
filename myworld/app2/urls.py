from django.urls import path
from .import views
app_name = 'app2'

urlpatterns = [
    path('signup', views.member.as_view(), name="signup"),
    path('', views.loginUser.as_view(), name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('order', views.order.as_view(), name="order"),
    path('forgetPass', views.forgetPass, name="forgetPass"),
    path('index', views.index, name="index"),
    path('blank', views.blank, name="blank"),
    path('buttons', views.buttons, name="buttons"),
    path('cards', views.cards, name="cards"),
    path('charts', views.charts, name="charts"),
    path('tables', views.tables, name="tables"),
    path('utilities_animation', views.utilities_animation, name="utilities_animation"),
    path('utilities_border', views.utilities_border, name="utilities_border"),
    path('utilities_color', views.utilities_color, name="utilities_color"), 
    path('utilities_other', views.utilities_other, name="utilities_other"),

]
