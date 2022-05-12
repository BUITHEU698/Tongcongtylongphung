from django.urls import path
from .import views
app_name = 'app2'

urlpatterns = [
    path('signup', views.member.as_view(), name="signup"),
    path('', views.loginUser.as_view(), name="login"),
    path('index', views.index, name="index"),
    path('blank', views.blank, name="blank"),
    path('more_products', views.more_products.as_view(), name="more_products"),
    path('list_products', views.list_products.as_view(), name="list_products"),
    
    path('more_product_portfolio', views.more_product_portfolio.as_view(),
         name="more_product_portfolio"),
    
    
    path('updata_product_portfolio/<int:id>', views.updata_product_portfolio.as_view(),
         name="updata_product_portfolio"),
    
    path('list_product_portfolio', views.list_product_portfolio.as_view(), name="list_product_portfolio"),

    path('cards', views.cards, name="cards"),
    path('charts', views.charts, name="charts"),
    path('tables', views.tables, name="tables"),
    path('utilities_animation', views.utilities_animation,name="utilities_animation"),
    path('utilities_border', views.utilities_border, name="utilities_border"),
    path('utilities_color', views.utilities_color, name="utilities_color"),
    path('utilities_other', views.utilities_other, name="utilities_other"),

]
 