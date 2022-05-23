from ast import If
from audioop import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import UserForm, contactForm, loginForm, CartItemForm, OrderForm
from .models import UserModel, contactModel, postBlog, CartModel, CartItemModel, OrderModel
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
        USER = -1
        template = loginForm
        thongbao = 'None'
        return render(request, 'userlogin.html', {'userLogin': template,
          'thongbao':thongbao})

    def post(self, request):
        if request.method == "POST":
            thongbao = 'None'
            userName = request.POST['userName']
            password = request.POST['password']

            user = UserModel.objects.filter(
                userName=userName, password=password).values()
            print(user)
            if user.count() == 1:
                for item in user:
                    global USER
                    USER = item
                context = {
                    'USER': USER
                }
                return redirect('app1:index')
                # return render(request, 'index.html', context)
            else:
                thongbao = "Mật khẩu hoặc tài khoản không đúng"
                context = {'thongbao': thongbao,
                           'password': password,
                           'userName': userName,
                           }
                return render(request, 'userlogin.html', context)


def forgetPass(request):
    template = loader.get_template('forgot-password.html')
    return HttpResponse(template.render())


class index(View):
    def get(self, request):
        cartModel = CartModel.objects.all().values()
        if USER == -1:
            USER2 = USER
            context = { 'USER': USER,
                        'listPortfolio': PortfolioModel.objects.all(),
                        'listproducts': ProductsModel.objects.all(),
                        'listUser': UserModel.objects.all(),
                        'timeNow': datetime.now(),
                   
                       }
            return render(request, 'index.html', context)
        else:
            for item in cartModel:
                if item["user_id"] == USER['id']:
                    context = {
                        'cartItemModel':  CartItemModel.objects.all(),
                        'listPortfolio': PortfolioModel.objects.all(),
                        'listproducts': ProductsModel.objects.all(),
                        'listUser': UserModel.objects.all(),
                        'timeNow': datetime.now(),
                        'myCart':  item,
                        'USER': USER
                    }
                    return render(request, 'index.html', context)
            f = CartModel(user_id=USER['id'])
            f.save()
            context = {'cartItemModel':  CartItemModel.objects.all(),
                    'listPortfolio': PortfolioModel.objects.all(),
                    'listproducts': ProductsModel.objects.all(),
                    'listUser': UserModel.objects.all(),
                    'timeNow': datetime.now(),
                    'myCart':  item,
                    'USER': USER
                    }
            return render(request, 'index.html', context)

    def post(self, request):
        cartItemModel = CartItemModel.objects.all()
        if request.method == "POST":
            cart = request.POST['cart']
            products = request.POST['products']
            quantile = request.POST['quantile']
            listCartItem = CartItemModel.objects.filter(
                products_id=products).values()
            if listCartItem.count() > 0:
                myCartItem = CartItemModel.objects.get(
                    id=listCartItem[0]['id'])
                myCartItem.quantile = myCartItem.quantile + int(quantile)
                myCartItem.save()
                return render(request, 'index.html')
            else:
                cartItem = CartItemModel(
                    cart_id=cart, products_id=products, quantile=quantile)
                cartItem.save()
            return render(request, 'index.html')
        else:
            return HttpResponse("no save success")


# --------------index-------------


def sitemap(request):
    template = loader.get_template('sitemap.xml')
    return HttpResponse(template.render())


# --------------cart-------------


# --------------checkout----------


class checkout(View):
    def get(self, request):
        cartModel = CartModel.objects.all().values()
        for item in cartModel:
            if item["user_id"] == USER['id']:
                tongTien = 0
                tienVanChuyen = 0
                listCartItem = CartItemModel.objects.filter(
                    cart_id=item["id"]).values()
                for i in listCartItem:
                    productCart = ProductsModel.objects.filter(
                        id=i['products_id']).values()
                    tongTien = productCart[0]['productsPrice'] * \
                        i['quantile'] + tongTien
                    tienVanChuyen = productCart[0]['weight'] + tienVanChuyen
                tienVanChuyen = tienVanChuyen*10000
                tongCong = tongTien + tienVanChuyen
                context = {'CartModel':  CartModel.objects.all(),
                           'tongTien': tongTien,
                           'cf': contactForm,
                           'tienVanChuyen': tienVanChuyen,
                           'tongCong': tongCong,
                           'listPortfolio': PortfolioModel.objects.all(),
                           'listproducts': ProductsModel.objects.all(),
                           'listUser': UserModel.objects.all(),
                           'timeNow': datetime.now(),
                           'USER': USER,
                           'myCart':  item,
                           'cartItemModel':  CartItemModel.objects.all(),
                           'listCartItem': CartItemModel.objects.filter(cart_id=item["id"])
                           }

                return render(request, 'checkout.html', context)

    def post(self, request):
        if request.method == "POST":
            if USER == -1:
                context = { 'USER' : USER}
                return render(request, 'userLogin.html', context)
            else:
                
                cartModel = CartModel.objects.filter(user_id=USER['id']).values()
                cf = OrderForm(request.POST)
                print(cf)
                # save_cf = OrderModel(cart_id = cartModel[0]['id'], ShipAddress=cf.cleaned_data['ShipAddress'],
                #                         order_description= cf.cleaned_data ['oder_description'], pay= cf.cleaned_data ['pay'])
                # save_cf.save()
                return render(request, 'checkout.html')


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


def blogDetail(request, id):
    template = postBlog.objects.get(id=id)
    return render(request, 'blogDetail.html', {'blogDetail': template})


# --------------logOut-------------


def logoutUser(request):
    logout(request)
    return redirect('app1:login')


class register(View):
    def get(self, request):
        thongbao = 'None'
        context = {'register': UserForm,
                   'USER': USER,
                   'thongbao': thongbao}
        return render(request, 'register.html', context)

    def post(self, request):
        if request.method == "POST":
            thongbao = 'None'
            userName = request.POST['userName']
            password = request.POST['password']
            email = request.POST['email']
            phoneNumber = request.POST['phoneNumber']
            resetpassword = request.POST['resetpassword']
            user = UserModel.objects.filter(userName=userName).values()
            if user.count() == 1:
                thongbao = "Tên tài khoản đã tồn tại. Mời nhập lại tên"
                context = {'thongbao': thongbao,
                           'email': email,
                           'phoneNumber': phoneNumber,
                           'password': password,
                           'resetpassword': resetpassword,
                           'userName': userName,
                           }
                return render(request, 'register.html', context)
            elif password != resetpassword:
                thongbao = "Mật khẩu không không trùng khớp. Mời kiểm tra và nhập lại"
                context = {'thongbao': thongbao,
                           'email': email,
                           'phoneNumber': phoneNumber,
                           'password': password,
                           'resetpassword': resetpassword,
                           'userName': userName,
                           }
                return render(request, 'register.html', context)
            elif len(phoneNumber) < 10 or len(phoneNumber) >= 12:
                thongbao = "Độ dài số điện thoại không hợp lệ"
                context = {'thongbao': thongbao,
                           'email': email,
                           'phoneNumber': phoneNumber,
                           'password': password,
                           'resetpassword': resetpassword,
                           'userName': userName,
                           }
                return render(request, 'register.html', context)
            elif phoneNumber.isdigit() == 0:
                thongbao = "Số điện thoại không bao gồm chữ cái"
                context = {'thongbao': thongbao,
                           'email': email,
                           'phoneNumber': phoneNumber,
                           'password': password,
                           'resetpassword': resetpassword,
                           'userName': userName,
                           }
                return render(request, 'register.html', context)
            else:
                f = UserForm(request.POST)
                if f.is_valid():
                    f.save()
                    print('haha')
                    print(f)
                    print('hihihi')
                    return redirect('app1:userLogin')
                else:
                    return HttpResponse("no save success")
        else:
            return HttpResponse("not POST")

# userName = request.POST['userName']
#             password = request.POST['password']

#             user = UserModel.objects.filter(
#                 userName=userName, password=password).values()
#             print(user)
#             if user.count() == 1:
#                 for item in user:
#                     global USER
#                     USER = item
#                 context = {
#                     'USER': USER
#                 }
#                 return redirect('app1:index')
#                 # return render(request, 'index.html', context)
#             else:
#                 return HttpResponse('Email hoặc mật khẩu của bạn không đúng')



class cart(View):
    def get(self, request):
        cartModel = CartModel.objects.all().values()
        if USER == -1:
            context = { 'USER' : USER}
            # return render(request, 'userLogin.html', context)
            return redirect('app1:userLogin')
        else:
            for item in cartModel:
                if item["user_id"] == USER['id']:
                    tongTien = 0
                    tienVanChuyen = 0
                    listCartItem = CartItemModel.objects.filter(
                        cart_id=item["id"]).values()
                    for i in listCartItem:
                        productCart = ProductsModel.objects.filter(
                            id=i['products_id']).values()
                        tongTien = productCart[0]['productsPrice'] * \
                            i['quantile'] + tongTien
                        tienVanChuyen = productCart[0]['weight'] + tienVanChuyen
                    tienVanChuyen = tienVanChuyen*10000
                    tongCong = tongTien + tienVanChuyen
                    context = {'CartModel':  CartModel.objects.all(),
                            'tongTien': tongTien,
                            'tienVanChuyen': tienVanChuyen,
                            'tongCong': tongCong,
                            'listPortfolio': PortfolioModel.objects.all(),
                            'listproducts': ProductsModel.objects.all(),
                            'listUser': UserModel.objects.all(),
                            'timeNow': datetime.now(),
                            'USER': USER,
                            'myCart':  item,
                            'cartItemModel':  CartItemModel.objects.all(),
                            'listCartItem': CartItemModel.objects.filter(cart_id=item["id"])
                            }

                    return render(request, 'cart.html', context)
            f = CartModel(user_id=USER['id'])
            f.save()
            context = {'CartModel':  CartModel.objects.all(),
                    'listPortfolio': PortfolioModel.objects.all(),
                    'listproducts': ProductsModel.objects.all(),
                    'listUser': UserModel.objects.all(),
                    'timeNow': datetime.now(),
                    'USER': USER,
                    'myCart':  f,
                    'cartItemModel':  CartItemModel.objects.all(),
                    'listCartItem': CartItemModel.objects.filter(cart_id=item["id"])
                    }
            return render(request, 'cart.html', context)

    def post(self, request):
        if request.method == "POST":
            IdCartItemModel = request.POST['id']
            myCartItem = CartItemModel.objects.get(id=IdCartItemModel)
            tg = request.POST['tg']
            if int(tg) == 0:
                print("da xoa")
                myCartItem.delete()
                return redirect('app1:cart')
            else:
                myCartItem.quantile = myCartItem.quantile + int(tg)
                myCartItem.save()
                if myCartItem.quantile == 0:
                    myCartItem.delete()
                return redirect('app1:cart')
