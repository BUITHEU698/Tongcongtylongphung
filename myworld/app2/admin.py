from django.contrib import admin
from .models import PortfolioModel
from .models import ProductsModel
# Register your models here.

admin.site.register(PortfolioModel)
admin.site.register(ProductsModel)
