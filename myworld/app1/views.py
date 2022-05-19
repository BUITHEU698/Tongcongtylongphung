from ast import If
from audioop import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import UserForm, contactForm, loginForm
from .models import UserModel, contactModel, postBlog, CartModel, CartItemModel
from app2.models import ProductsModel, PortfolioModel
from app2.forms import PortfolioForm, ProductsForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
# --------------index-------------
global USER
USER = -1


class userLogin (View):
    def get(self, request):
        template = loginForm
        return render(request, 'userlogin.html', {'userLogin': template})

    def post(self, request):
        if request.method == "POST":
            userName = request.POST['userName']
            password = request.POST['password']

            user = UserModel.objects.filter(
                userName=userName, password=password).values()

            if user.count() == 1:
                for item in user:
                    global USER
                    USER = item
                context = {
                    'USER': USER
                }
                return render(request, 'index.html', context)
            else:
                return HttpResponse('Email hoặc mật khẩu của bạn không đúng')


def forgetPass(request):
    template = loader.get_template('forgot-password.html')
    return HttpResponse(template.render())


class index(LoginRequiredMixin, View):
    login_url = 'app1:userLogin'

    def get(self, request):
        context = {
            'listPortfolio': PortfolioModel.objects.all(),
            'listproducts': ProductsModel.objects.all(),
            'listUser': UserModel.objects.all(),
            'timeNow': datetime.now(),
            'USER': USER
        }
        return render(request, 'index.html', context)


# --------------index-------------


def sitemap(request):
    template = loader.get_template('sitemap.xml')
    return HttpResponse(template.render())


# --------------cart-------------


# --------------checkout-------------
def checkout(request):
    template = loader.get_template('checkout.html')
    return HttpResponse(template.render())


# --------------contact-------------

class contact(View):
    def get(self, request):

        context = {'cf': contactForm,
                   'listPortfolio': PortfolioModel.objects.all(),
                   'USER': USER
                   }
        return render(request, 'contact.html', context)

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
                return render(request, 'thanks.html')
        else:
            return HttpResponse("not POST")


def thanks(request):
    template = loader.get_template('thanks.html')
    return HttpResponse(template.render())
# --------------shop-------------


class shop(View):
    def get(self, request):
        context = {
            'listPortfolio': PortfolioModel.objects.all(),
            'listproducts': ProductsModel.objects.all(),
            'listUser': UserModel.objects.all(),
            'timeNow': datetime.now(),
            'USER': USER
        }

        return render(request, 'shop.html', context)


# --------------detail-------------


class detailProduct(View):
    def get(self, request, id):
        context = {
            'myProduct':  ProductsModel.objects.get(id=id),
            'USER': USER
        }
        return render(request, 'detail.html', context)

# --------------blog-------------


class blog(View):
    def get(self, request):
        context = {
            'listPortfolio': PortfolioModel.objects.all(),
            'listUser': UserModel.objects.all(),
            'timeNow': datetime.now(),
            'USER': USER
        }

        return render(request, 'blog.html', context)


class blog1(View):
    def get(self, request):
        context = {
            'listPortfolio': PortfolioModel.objects.all(),
            'listUser': UserModel.objects.all(),
            'timeNow': datetime.now(),
            'USER': USER
        }

        return render(request, 'blog1.html', context)


class blog2(View):
    def get(self, request):
        context = {
            'listPortfolio': PortfolioModel.objects.all(),
            'listUser': UserModel.objects.all(),
            'timeNow': datetime.now(),
            'USER': USER
        }

        return render(request, 'blog2.html', context)


class blog3(View):
    def get(self, request):
        context = {
            'listPortfolio': PortfolioModel.objects.all(),
            'listUser': UserModel.objects.all(),
            'timeNow': datetime.now(),
            'USER': USER
        }

        return render(request, 'blog3.html', context)


class blog4(View):
    def get(self, request):
        context = {
            'listPortfolio': PortfolioModel.objects.all(),
            'listUser': UserModel.objects.all(),
            'timeNow': datetime.now(),
            'USER': USER
        }

        return render(request, 'blog4.html', context)


def blogDetail(request, id):
    template = postBlog.objects.get(id=id)
    return render(request, 'blogDetail.html', {'blogDetail': template})


# --------------logOut-------------


def logoutUser(request):
    logout(request)
    return redirect('app2:login')


class register(View):
    def get(self, request):
        context = {'register': UserForm,
                   'USER': USER}
        return render(request, 'register.html', context)

    def post(self, request):
        if request.method == "POST":
            f = UserForm(request.POST)
            if f.is_valid():
                f.save()
                return redirect('app1:userLogin')
            else:
                return HttpResponse("no save success")
        else:
            return HttpResponse("not POST")


class cart(View):
    def get(self, request):
        context = {'CartModel': CartModel,
                   'listPortfolio': PortfolioModel.objects.all(),
                   'listproducts': ProductsModel.objects.all(),
                   'listUser': UserModel.objects.all(),
                   'timeNow': datetime.now(),
                   'USER': USER}

        return render(request, 'cart.html', context)


class cart(View):
    def get(self, request):
        cartModel = CartModel.objects.all().values()
        for item in cartModel:
            if item["user_id"] == USER['id']:
                print(item["user_id"])
                print('hahaha')
                print(USER['id'])
                context = {'CartModel':  CartModel.objects.all(),
                           'listPortfolio': PortfolioModel.objects.all(),
                           'listproducts': ProductsModel.objects.all(),
                           'listUser': UserModel.objects.all(),
                           'timeNow': datetime.now(),
                           'USER': USER,
                           'myCart':  item
                           }
                return render(request, 'cart.html', context)
        f = CartModel(user_id = USER['id'])
        f.save()
        context = {'CartModel':  CartModel.objects.all(),
                   'listPortfolio': PortfolioModel.objects.all(),
                   'listproducts': ProductsModel.objects.all(),
                   'listUser': UserModel.objects.all(),
                   'timeNow': datetime.now(),
                   'USER': USER,
                   'myCart':  f,
                   'CartItemModel':  CartItemModel.objects.all(),
                   }
        return render(request, 'cart.html', context)
