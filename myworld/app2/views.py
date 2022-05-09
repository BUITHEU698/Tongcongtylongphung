from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import memberForm
from .forms import loginForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# --------------login-------------


# --------------blog-------------
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

# --------------blog-------------


class loginUser (View):
    def get(self, request):
        template = loginForm
        return render(request, 'login2.html', {'login': template})

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
    template = loader.get_template('forgetPass.html')
    return HttpResponse(template.render())


# --------------index-------------


def index(request):
    template = loader.get_template('index2.html')
    return HttpResponse(template.render())


# --------------calendar-------------
def calendar(request):
    template = loader.get_template('calendar.html')
    return HttpResponse(template.render())


# --------------chart-------------
def chart(request):
    template = loader.get_template('chart.html')
    return HttpResponse(template.render())



# --------------inbox-------------
def inbox(request):
    template = loader.get_template('inbox.html')
    return HttpResponse(template.render())


# --------------map-------------
def map(request):
    template = loader.get_template('map.html')
    return HttpResponse(template.render())

# --------------switch-------------
def switch(request):
    template = loader.get_template('switch.html')
    return HttpResponse(template.render())

# --------------tab-------------
def tab(request):
    template = loader.get_template('tab.html')
    return HttpResponse(template.render())

# --------------table-------------
def table(request):
    template = loader.get_template('table.html')
    return HttpResponse(template.render())