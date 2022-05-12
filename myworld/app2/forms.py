from django import forms
from .models import PortfolioModel
from .models import ProductsModel

# --------------memberForm-------------

class memberForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    # phone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
# --------------memberForm-------------


class loginForm(forms.Form):
    email = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)



class PortfolioForm (forms.ModelForm):
    class Meta:
        model = PortfolioModel
        fields = {'portfolioName','portfolioBody','portfolioPub','portfolioTimePub','portfolioImg' }


class ProductsForm (forms.ModelForm):
    class Meta:
        model = ProductsModel
        fields = {'productsName','productsBody','productsImg','productsPrice','productsPriceOther','inventory','productsPub','productsTimePub','portfolioModel','weight' }


