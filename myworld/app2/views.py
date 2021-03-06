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
from django.contrib.auth import authenticate, login, logout, decorators
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from app1.models import OrderModel, UserModel, CartModel


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


# --------------index-------------
@decorators.login_required(login_url='app2:login')
def index(request):
    template = loader.get_template('index2.html')
    return HttpResponse(template.render())


# --------------blank.html-------------

@decorators.login_required(login_url='app2:login')
def forgetPass(request):
    template = loader.get_template('forgetPass.html')
    return HttpResponse(template.render())


# --------------products-------------\

class more_products(LoginRequiredMixin, View):
    login_url = 'app2:login'

    def get(self, request):
        context = {'cp': ProductsForm,
                   'listPortfolio': PortfolioModel.objects.all(),
                   'timeNow': datetime.now().strftime('%Y-%m-%dT%H:%M')
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


class list_products(LoginRequiredMixin, View):
    login_url = 'app2:login'

    def get(self, request):
        context = {
            'list_products': ProductsModel.objects.all(),
            'timeNow': datetime.now(),

        }
        return render(request, 'list_products.html', context)

    def post(self, request):
        if request.method == "POST":
            CheckBox = request.POST.getlist('CheckBox')
            for item in CheckBox:
                delete = ProductsModel.objects.get(id=item)
                delete.delete()
        return HttpResponseRedirect(reverse('app2:list_products'))


class updata_product(LoginRequiredMixin, View):
    login_url = 'app2:login'

    def get(self, request, id):
        context = {
            'myProduct':  ProductsModel.objects.get(id=id),
            'listPortfolio': PortfolioModel.objects.all(),
            'myProductsTimePub':  ProductsModel.objects.get(id=id).productsTimePub.strftime('%Y-%m-%dT%H:%M')
        }
        return render(request, 'update_products.html', context)

    def post(self, request, id):
        myProduct = ProductsModel.objects.get(id=id)
        if request.method == "POST":
            myProduct.productsName = request.POST['productsName']
            myProduct.productsBody = request.POST['productsBody']
            # myProduct.productsImg = request.POST['productsImg']
            myProduct.productsPrice = request.POST['productsPrice']
            myProduct.productsPriceOther = request.POST['productsPriceOther']
            myProduct.inventory = request.POST['inventory']
            myProduct.productsTimePub = request.POST['productsTimePub']
            myProduct.portfolioModel_id = request.POST['portfolioModel']
            myProduct.weight = request.POST['weight']
            myProduct.save()
        context = {
            'myProduct':  ProductsModel.objects.get(id=id),
            'listPortfolio': PortfolioModel.objects.all(),
            'myProductsTimePub':  ProductsModel.objects.get(id=id).productsTimePub.strftime('%Y-%m-%dT%H:%M')
        }
        return render(request, 'update_products.html', context)

# --------------portfolio-------------


class updata_product_portfolio(LoginRequiredMixin, View):
    login_url = 'app2:login'

    def get(self, request, id):
        context = {
            'myPortfolio':  PortfolioModel.objects.get(id=id),
            'myPortfolioTimePub':  PortfolioModel.objects.get(id=id).portfolioTimePub.strftime('%Y-%m-%dT%H:%M')
        }
        return render(request, 'updata_product_portfolio.html', context)

    def post(self, request, id):
        myPortfolio = PortfolioModel.objects.get(id=id)
        if request.method == "POST":
            myPortfolio.portfolioName = request.POST['portfolioName']
            myPortfolio.portfolioBody = request.POST['portfolioBody']
            # myPortfolio.portfolioImg = request.POST['portfolioImg']
            myPortfolio.portfolioTimePub = request.POST['portfolioTimePub']
            myPortfolio.save()
        context = {
            'myPortfolio':  PortfolioModel.objects.get(id=id),
            'listPortfolio': PortfolioModel.objects.all(),
            'myPortfolioTimePub':  PortfolioModel.objects.get(id=id).portfolioTimePub.strftime('%Y-%m-%dT%H:%M')
        }
        return render(request, 'updata_product_portfolio.html', context)


class more_product_portfolio(LoginRequiredMixin, View):
    login_url = 'app2:login'

    def get(self, request):
        context = {'cf': PortfolioForm,
                   'timeNow': datetime.now().strftime('%Y-%m-%dT%H:%M')}
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


class list_product_portfolio(LoginRequiredMixin, View):
    login_url = 'app2:login'

    def get(self, request):
        context = {
            'listProducts': ProductsModel.objects.all(),
            'listPortfolio': PortfolioModel.objects.all(),
            'timeNow': datetime.now(),
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


class orderMenu(LoginRequiredMixin, View):
    login_url = 'app2:login'

    def get(self, request):
        orderMenu = OrderModel.objects.all()

        context = {
            'listUser': UserModel.objects.all(),
            'timeNow': datetime.now(),
            'orderMenu': orderMenu
        }

        return render(request, 'orderMenu.html', context)

# --------------utilities_animation-------------


class userMenu(LoginRequiredMixin, View):
    login_url = 'app2:login'

    def get(self, request):
        orderMenu = OrderModel.objects.all().values()
        listUser = UserModel.objects.all().values()
        a = []
        soLuong = 0
        sotien = 0
        for item in listUser:
            CartUser = CartModel.objects.filter(user_id=item['id']).values()
            listOrderUser = OrderModel.objects.filter(
                cart_id=CartUser[0]['id']).values()     
            for item2 in listOrderUser:
                soLuong = soLuong + 1
                sotien = sotien + item2['tongCong']
            a.append({'id': int(item['id']),  'soLuong': int(soLuong), 'sotien': int(sotien)})

            print(a)

        context = {
            'listUser': UserModel.objects.all(),
            'timeNow': datetime.now(),
            'a': a,
            'orderMenu': orderMenu
        }

        return render(request, 'userMenu.html', context)
