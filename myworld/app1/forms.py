from django import forms
from .models import UserModel,CartItemModel, OrderModel

# --------------contact-------------
class contactForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

class OrderForm (forms.ModelForm):
     class Meta:
        model = OrderModel
        fields = {'user','ShipAddress','order_description','pay'}
   

class UserForm (forms.ModelForm):
    class Meta:
        model = UserModel
        fields = {'userName','email','phoneNumber','password' ,'resetpassword'}
        widgets = {
        'password': forms.PasswordInput(),
        'resetpassword': forms.PasswordInput()
            }
        
class CartItemForm (forms.ModelForm):
    class Meta:
        model = CartItemModel
        fields = {'cart','products','quantile'}
       

# # --------------memberForm-------------

# class memberForm(forms.Form):
#     username = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length = 30)
#     # phone = forms.CharField(max_length=11)
#     password = forms.CharField(max_length=20, widget = forms.PasswordInput)
# # --------------memberForm-------------


class loginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = {'userName','password' ,}
        widgets = {
        'password': forms.PasswordInput(),
       
            }
