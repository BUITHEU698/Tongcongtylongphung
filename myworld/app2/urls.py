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
    path('calendar', views.calendar, name="calendar"),
    path('chart', views.chart, name="chart"),
    path('inbox', views.inbox, name="inbox"),
    path('map', views.map, name="map"),
    path('switch', views.switch, name="switch"),
    path('tab', views.tab, name="tab"),
    path('table', views.table, name="table"),

]
