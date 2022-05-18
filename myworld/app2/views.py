from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import memberForm
from .forms import loginForm
from .forms import PortfolioForm
from .forms import ProductsForm
from .models import PortfolioModel
from .models import ProductsModel
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime


class loginUser (View):
    def get(self, request):
        template = loginForm
        return render(request, 'login.html', {'login': template})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app2:index')

        else:
            return HttpResponse('Email hoặc mật khẩu của bạn không đúng')


def forgetPass(request):
    template = loader.get_template('forgot-password.html')
    return HttpResponse(template.render())


# --------------index-------------


def index(request):
    template = loader.get_template('index2.html')
    return HttpResponse(template.render())


# --------------blank.html-------------


def blank(request):
    template = loader.get_template('blank.html')
    return HttpResponse(template.render())


# --------------products-------------
class more_products(View):
    def get(self, request):
        context = {'cp': ProductsForm,
                   'listPortfolio': PortfolioModel.objects.all(),
                   'timeNow' : datetime.now().strftime('%Y-%m-%dT%H:%M')   
                   }
        return render(request, 'more_products.html', context)

    def post(self, request):
        if request.method == "POST":
            f = ProductsForm(request.POST, request.FILES)
            if f.is_valid():
                f.save()
                return HttpResponseRedirect(reverse('app2:list_products'))
            else:
                return HttpResponse("no save success")
        else:
            return HttpResponse("not POST")


class list_products(View):
    def get(self, request):
        context = {
            'list_products': ProductsModel.objects.all(),
            'timeNow' : datetime.now(),
            
        }
        return render(request, 'list_products.html', context)
    def post(self, request):
        if request.method == "POST":
            CheckBox = request.POST.getlist('CheckBox')
            for item in CheckBox:
                delete = ProductsModel.objects.get(id=item)
                delete.delete()
        return HttpResponseRedirect(reverse('app2:list_products'))

class updata_product(View):
    def get(self, request, id):
        context = {
            'myProduct':  ProductsModel.objects.get(id=id),
            'listPortfolio': PortfolioModel.objects.all(),
            'myProductsTimePub' :  ProductsModel.objects.get(id=id).productsTimePub.strftime('%Y-%m-%dT%H:%M')   
        }
        return render(request, 'update_products.html', context)
    
    def post(self, request, id):
        myProduct =   ProductsModel.objects.get(id=id)
        if request.method == "POST":
            myProduct.productsName = request.POST['productsName']
            myProduct.productsBody = request.POST['productsBody']
            # myProduct.productsImg = request.POST['productsImg']
            myProduct.productsPrice = request.POST['productsPrice']
            myProduct.productsPriceOther = request.POST['productsPriceOther']
            myProduct.inventory = request.POST['inventory']
            myProduct.productsTimePub = request.POST['productsTimePub']
            # myProduct.portfolioModel = request.POST['portfolioModel']
            myProduct.weight = request.POST['weight']
            myProduct.save()
        context = {
            'myProduct':  ProductsModel.objects.get(id=id),
            'listPortfolio': PortfolioModel.objects.all(),
             'myProductsTimePub' :  ProductsModel.objects.get(id=id).productsTimePub.strftime('%Y-%m-%dT%H:%M')   
        }
        return render(request, 'update_products.html', context)

# --------------portfolio-------------
class updata_product_portfolio(View):
    def get(self, request, id):
        context = {
            'myPortfolio':  PortfolioModel.objects.get(id=id),
            'myPortfolioTimePub' :  PortfolioModel.objects.get(id=id).portfolioTimePub.strftime('%Y-%m-%dT%H:%M')      
        }
        return render(request, 'updata_product_portfolio.html', context)

    def post(self, request, id):
        myPortfolio =   PortfolioModel.objects.get(id=id)
        if request.method == "POST":
            myPortfolio.portfolioName = request.POST['portfolioName']
            myPortfolio.portfolioBody = request.POST['portfolioBody']
            # myPortfolio.portfolioImg = request.POST['portfolioImg']
            myPortfolio.portfolioTimePub = request.POST['portfolioTimePub']
            myPortfolio.save()
        context = {
            'myPortfolio':  PortfolioModel.objects.get(id=id),      
            'listPortfolio': PortfolioModel.objects.all(),
            'myPortfolioTimePub' :  PortfolioModel.objects.get(id=id).portfolioTimePub.strftime('%Y-%m-%dT%H:%M')      
        }
        return render(request, 'updata_product_portfolio.html', context)


class more_product_portfolio(View):
    def get(self, request):
        context = {'cf': PortfolioForm,
                   'timeNow' : datetime.now().strftime('%Y-%m-%dT%H:%M')  }
        return render(request, 'more_product_portfolio.html', context)

    def post(self, request):
        if request.method == "POST":
            f = PortfolioForm(request.POST, request.FILES)
            if f.is_valid():
                f.save()
                return HttpResponseRedirect(reverse('app2:list_product_portfolio'))
            else:
                return HttpResponse("no save success")
        else:
            return HttpResponse("not POST")


class list_product_portfolio(View):
    def get(self, request):     
        context = {
            'listProducts': ProductsModel.objects.all(),
            'listPortfolio': PortfolioModel.objects.all(),
            'timeNow' : datetime.now(),
        }
    
        return render(request, 'list_product_portfolio.html', context)
    def post(self, request):
            if request.method == "POST":
                CheckBox = request.POST.getlist('CheckBox')
                for item in CheckBox:
                    delete = PortfolioModel.objects.get(id=item)
                    delete.delete()
            return HttpResponseRedirect(reverse('app2:list_product_portfolio'))

# --------------charts-------------

def cards(request):
    template = loader.get_template('cards.html')
    return HttpResponse(template.render())


# --------------charts-------------
def charts(request):
    template = loader.get_template('charts.html')
    return HttpResponse(template.render())
# --------------tables-------------


def tables(request):
    template = loader.get_template('tables.html')
    return HttpResponse(template.render())

# --------------utilities_animation-------------


def utilities_animation(request):
    template = loader.get_template('utilities_animation.html')
    return HttpResponse(template.render())

# --------------utilities_border-------------


def utilities_border(request):
    template = loader.get_template('utilities_border.html')
    return HttpResponse(template.render())

# --------------utilities_color.html-------------


def utilities_color(request):
    template = loader.get_template('utilities_color.html')
    return HttpResponse(template.render())

# --------------utilities_other.html-------------


def utilities_other(request):
    template = loader.get_template('utilities_other.html')
    return HttpResponse(template.render())
