from django.urls import path
from .import views
app_name = 'app2'

urlpatterns = [
    #     path('signup', views.member.as_view(), name="signup"),
    path('', views.loginUser.as_view(), name="login"),
    path('index', views.index, name="index"),
    path('more_products', views.more_products.as_view(), name="more_products"),
    path('list_products', views.list_products.as_view(), name="list_products"),
    path('more_product_portfolio', views.more_product_portfolio.as_view(),
         name="more_product_portfolio"),
    path('updata_product_portfolio/<int:id>', views.updata_product_portfolio.as_view(),
         name="updata_product_portfolio"),

    path('updata_product/<int:id>', views.updata_product.as_view(),
         name="updata_product"),

    path('list_product_portfolio', views.list_product_portfolio.as_view(),
         name="list_product_portfolio"),
    path('orderMenu', views.orderMenu.as_view(), name="orderMenu"),
    path('userMenu', views.userMenu.as_view(), name="userMenu"),
    path('forgetPass', views.forgetPass, name="forgetPass"),


]
