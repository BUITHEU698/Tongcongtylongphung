from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from app2.models import ProductsModel, PortfolioModel
from django.utils import timezone


class CheckoutSitemap(Sitemap):
    priority = 0.5
    def items(self):
        return['app1:checkout',
               'app1:cart',
               'app1:contact',
               'app1:thanks',
               'app1:shop',
               'app1:blog',
               'app1:blog1',
               'app1:blog2',
               'app1:blog3',
               'app1:menuOrder',
               'app1:userLogin',
               'app1:register',
               'app1:forgetPass',
               ]

    def lastmod(self, item):
        return timezone.now()

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    priority = 0.5
    def items(self):
        return ProductsModel.objects.all()
    def lastmod(self, item):
        return timezone.now()

    # def lastmod(self, obj):
    #     return obj.productsName
