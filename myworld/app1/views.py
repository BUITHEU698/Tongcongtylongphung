from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import contactForm
from .models import contactModel
from .models import postBlog
from app2.models import ProductsModel
from app2.models import PortfolioModel
from app2.forms import PortfolioForm
from app2.forms import ProductsForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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


def shop(request):
    template = loader.get_template('shop.html')
    return HttpResponse(template.render())

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

# # --------------member-------------
# class member(View):
#     def get(self, request):
#         template = memberForm
#         return render(request, 'signup.html', {'signup': template})

#     def post(self, request):
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']

#         user = User.objects.create_user(username, email, password)
#         user.save()
#         return HttpResponse('save sussic')

# # --------------loginUser-------------


# class loginUser (View):
#     def get(self, request):
#         template = loginForm
#         return render(request, 'login.html', {'login': template})

#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         try: 
#             user = authenticate(request, username=User.objects.get(
#                 email=username), password=password)
#         except:
#             user = authenticate(request, username = username, password = password)
            
#         if user is not None:
#             login(request, user)
#             return render(request, 'order.html')
#         else:
#             return HttpResponse('login fail')

# # --------------logOut-------------


# def logoutUser(request):
#     logout(request)
#     return redirect('app1:login')


# # --------------order-------------


# class order(LoginRequiredMixin, View):
#     login_url = '/login'
#     def get(self, request):
#         return render(request, 'order.html')
    
    
