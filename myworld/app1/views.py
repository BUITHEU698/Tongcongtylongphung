from re import template
from django.http import HttpRequest
from django.shortcuts import render
from matplotlib.style import context
from django.http import HttpResponse
from django.template import loader
from .backend.contact import contacForm

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
    context = {'cf':contacForm}
    return render(request, 'contact.html', context)
def getContact(request):
    if request.method:
        cf = contacForm(request.POST)
        if cf.is_valid():
            cf.save()
            return HttpResponse("save success")
    else:
        return HttpResponse("not POST")
        
        
    
    
 
def shop(request):
    template = loader.get_template('shop.html')
    return HttpResponse(template.render())

def detail(request):
    template = loader.get_template('detail.html')
    return HttpResponse(template.render())