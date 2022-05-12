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
# --------------login-------------


# --------------member-------------
class member(View):
    def get(self, request):
        template = memberForm
        return render(request, 'register.html', {'signup': template})

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('app2:login')

# --------------loginUser-------------


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

# --------------logOut-------------


def logoutUser(request):
    logout(request)
    return redirect('app2:login')


# --------------order-------------


class order(LoginRequiredMixin, View):
    login_url = '/login'

    def get(self, request):
        return render(request, 'index.html')


# --------------forget-paswork-------------


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
                   }
        return render(request, 'more_products.html', context)

    def post(self, request):
        if request.method == "POST":
            f = ProductsForm(request.POST, request.FILES)
            if f.is_valid():

                f.save()
                return HttpResponse("save success")
            else:
                return HttpResponse("no save success")
        else:
            return HttpResponse("not POST")


class list_products(View):
    def get(self, request):
        context = {
            'list_products': ProductsModel.objects.all(),
        }
        return render(request, 'list_products.html', context)


# --------------portfolio-------------
class updata_product_portfolio(View):
    def get(self, request, id):
        context = { 
                   'myPortfolio':  PortfolioModel.objects.get(id=id),
                   }
        return render(request, 'updata_product_portfolio.html', context)

    def updaterecord(self, request, id):
        context = {
            'myPortfolio':  PortfolioModel.objects.get(id=id),
            }
        if request.method == "POST":
            f = PortfolioForm(request.POST, request.FILES)
            if f.is_valid():
                myPortfolio = f
                myPortfolio.save()
                return HttpResponse("update success")
            else:
                return HttpResponse("no update success")
        else:
            return HttpResponse("not POST")
    




class more_product_portfolio(View):
    def get(self, request):
        context = {'cf': PortfolioForm}
        return render(request, 'more_product_portfolio.html', context)

    def post(self, request):
        if request.method == "POST":
            f = PortfolioForm(request.POST, request.FILES)
            if f.is_valid():

                f.save()
                return HttpResponse("save success")
            else:
                return HttpResponse("no save success")
        else:
            return HttpResponse("not POST")
        
class list_product_portfolio(View):
    def get(self, request):
        context = {
            'listPortfolio': PortfolioModel.objects.all(),
        }
        return render(request, 'list_product_portfolio.html', context)




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
