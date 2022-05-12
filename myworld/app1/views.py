from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import UserForm, contactForm
from .models import UserModel, contactModel
from .models import postBlog
from app2.models import ProductsModel
from app2.models import PortfolioModel
from app2.forms import PortfolioForm
from app2.forms import ProductsForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# --------------index-------------


class index(View):
    def get(self, request):
        context = {
            'listPortfolio': PortfolioModel.objects.all(),
            'listproducts': ProductsModel.objects.all(),
        }
        return render(request, 'index.html', context)


# --------------index-------------


def sitemap(request):
    template = loader.get_template('sitemap.xml')
    return HttpResponse(template.render())


# --------------cart-------------
@decorators.login_required(login_url='/userLogin/')
def cart(request):
    template = loader.get_template('cart.html')
    return HttpResponse(template.render())


# --------------checkout-------------
def checkout(request):
    template = loader.get_template('checkout.html')
    return HttpResponse(template.render())


# --------------contact-------------

class contact(View):
    def get(self, request):
        context = {'cf': contactForm}
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
                return HttpResponse("save success")
        else:
            return HttpResponse("not POST")

# --------------shop-------------


class shop(View):
    def get(self, request):
        context = {
            'listPortfolio': PortfolioModel.objects.all(),
            'listproducts': ProductsModel.objects.all(),
        }
        return render(request, 'shop.html', context)


# --------------detail-------------


def detail(request):
    template = loader.get_template('detail.html')
    return HttpResponse(template.render())

# --------------blog-------------


def blog(request):
    template = postBlog.objects.all()
    return render(request, 'blog.html', {'blog': template})


def blogDetail(request, id):
    template = postBlog.objects.get(id=id)
    return render(request, 'blogDetail.html', {'blogDetail': template})

# def blog1(request):
#     template = loader.get_template('blog1.html')
#     return HttpResponse(template.render())


def blog1(request):
    template = loader.get_template('blog1.html')
    return HttpResponse(template.render())


def blog2(request):
    template = loader.get_template('blog2.html')
    return HttpResponse(template.render())


def blog3(request):
    template = loader.get_template('blog3.html')
    return HttpResponse(template.render())


def blog4(request):
    template = loader.get_template('blog4.html')
    return HttpResponse(template.render())


class userLogin (View):
    def get(self, request):
        template = UserForm
        return render(request, 'userlogin.html', {'login': template})


class userLogin(View):
    def get(self, request):
        context = {
                        'UserModel': UserModel.objects.all(),
                   }
        return render(request, 'userLogin.html', context)
    
    
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

#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('app2:index')

#         else:
#             return HttpResponse('Email hoặc mật khẩu của bạn không đúng')


# def logoutUser(request):
#     logout(request)
#     return redirect('app1:userLogin')


# # --------------order-------------


# class order(LoginRequiredMixin, View):
#     login_url = '/userLogin'
#     def get(self, request):
#         return render(request, 'cart.html')
