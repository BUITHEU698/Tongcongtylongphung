from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import memberForm
from .forms import loginForm
from .forms import PortfolioForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
def more_products(request):
    template = loader.get_template('more_products.html')
    return HttpResponse(template.render())


def list_products(request):
    template = loader.get_template('list_products.html')
    return HttpResponse(template.render())


# def more_product_portfolio(request):
#     template = loader.get_template('more_product_portfolio.html')
#     return HttpResponse(template.render())

# # --------------shop-------------


class more_product_portfolio(View):
    def get(self, request):
        context = {'cf': PortfolioForm}
        return render(request, 'more_product_portfolio.html', context)

    def post(self, request):
        # kiem tra xem co phai phuong thuc post k
        if request.method == "POST":
            # gan thong tin cua contactForm nhap tu ban phim vao trong bien cf
            cf = contactForm(request.POST)
            # Kiem tra dieu kien nhap trong input: neu dieu kien dung
            if cf.is_valid():
                # chuyen doi thong tin cua form thanh thong tin cua model
                save_cf = contactModel(username=cf.cleaned_data['username'], email=cf.cleaned_data['email'],
                                       subject=cf.cleaned_data['subject'], message=cf.cleaned_data['message'])
                # luu thong tin vaao model
                save_cf.save()
                return HttpResponse("save success")
        else:
            return HttpResponse("not POST")

# --------------shop-------------

def list_product_portfolio(request):
    template = loader.get_template('list_product_portfolio.html')
    return HttpResponse(template.render())


# --------------cards-------------
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



