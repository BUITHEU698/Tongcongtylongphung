from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import contactForm
from .models import contactModel 

#--------------index-------------
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
    


#--------------cart-------------
def cart(request):
    template = loader.get_template('cart.html')
    return HttpResponse(template.render())



#--------------checkout-------------
def checkout(request):
    template = loader.get_template('checkout.html')
    return HttpResponse(template.render())


    
#--------------contact-------------
def contact(request):
    context = {'cf':contactForm}
    return render(request, 'contact.html', context)
        
def saveContact (re1uest):
    # kiem tra xem co phai phuong thuc post k
    if request.method == "POST":
        cf = contacForm(request.POST)
        # Kiem tra dieu kien nhap trong input
        if cf.is_valid():
            #chuyen doi thong tin cua form thanh thong tin cua model
            save_cf = contactModel(username) 
            #luu thong tin vaao model 
            cf.save()
            return HttpResponse("save success")
    else:
        return HttpResponse("not POST")
    
#--------------shop-------------    
def shop(request):
    template = loader.get_template('shop.html')
    return HttpResponse(template.render())

#--------------detail-------------  
def detail(request):
    template = loader.get_template('detail.html')
    return HttpResponse(template.render())