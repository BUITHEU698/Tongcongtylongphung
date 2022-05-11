from django import forms
from .models import PortfolioModel

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



class PortfolioForm (forms.Form):
    portfolioName = forms.CharField(max_length=200)
    portfolioBody = forms.CharField(widget=forms.Textarea)
    portfolioPub = forms.ChoiceField(
        label='Hiển Thị', widget=forms.RadioSelect, choices=PortfolioModel.CHOICES)
    portfolioTimePub = forms.DateTimeField()
    portfolioImg = forms.FileField()
     
