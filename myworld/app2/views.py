from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import memberForm
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
        return HttpResponse('save sussic')

# --------------blog-------------


class loginUser (View):
    def get(self, request):
        template = loginForm
        return render(request, 'login2.html', {'login': template})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username=User.objects.get(
                email=username), password=password)
        except:
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return HttpResponse('login fail')

# --------------logOut-------------


def logoutUser(request):
    logout(request)
    return redirect('app2:login')


# --------------order-------------


class order(LoginRequiredMixin, View):
    login_url = '/login'

    def get(self, request):
        return render(request, 'index.html')
