from ast import If
from audioop import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import UserForm, contactForm, loginForm
from .models import UserModel, contactModel, postBlog
from app2.models import ProductsModel, PortfolioModel
from app2.forms import PortfolioForm, ProductsForm
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
            'listUser': UserModel.objects.all(),
        }
        return render(request, 'index.html', context)


# --------------index-------------


def sitemap(request):
    template = loader.get_template('sitemap.xml')
    return HttpResponse(template.render())


# --------------cart-------------
# @decorators.login_required(login_url='/userLogin/')
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
        
        context = {'cf': contactForm,
                    'listPortfolio': PortfolioModel.objects.all(),
                   
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


    
    
# --------------logOut-------------


def logoutUser(request):
    logout(request)
    return redirect('app2:login')



    
class register(View):
    def get(self, request):
        context = {'register': UserForm,}
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

class userLogin (View):
    def get(self, request):
        template = loginForm
        return render(request, 'userlogin.html', {'userLogin': template})

    def post(self, request):
        if request.method == "POST":
            userName = request.POST['userName']
            password = request.POST['password']
        
            user = UserModel.objects.filter(userName=userName,password =password ).values()
            context = {
                    'user': user.count()
                   }
            if  user.count() ==1 :
                return redirect('app1:index')
            else:
                return HttpResponse('Email hoặc mật khẩu của bạn không đúng')
        
      

def forgetPass(request):
    template = loader.get_template('forgot-password.html')
    return HttpResponse(template.render())



