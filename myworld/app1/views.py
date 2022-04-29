from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import contactForm
from .models import contactModel
from django.views import View

# --------------index-------------


def index(request):
    template = loader.get_template('index.html')
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
    template = loader.get_template('blog.html')
    return HttpResponse(template.render())


def blog1(request):
    template = loader.get_template('blog1.html')
    return HttpResponse(template.render())


def blog2(request):
    template = loader.get_template('blog2.html')
    return HttpResponse(template.render())
