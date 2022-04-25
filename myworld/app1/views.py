from re import template
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
    

def cart(request):
    template = loader.get_template('cart.html')
    return HttpResponse(template.render())


def checkout(request):
    template = loader.get_template('checkout.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

 
def shop(request):
    template = loader.get_template('shop.html')
    return HttpResponse(template.render())

def detail(request):
    template = loader.get_template('detail.html')
    return HttpResponse(template.render())