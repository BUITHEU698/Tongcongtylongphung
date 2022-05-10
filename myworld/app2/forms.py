from django import forms

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


FRUIT_CHOICES = [
    ('1', 'Ẩn'),
    ('2', 'Hiện'),
]

class PortfolioForm (forms.Form):
    portfolioName = forms.CharField(max_length=200)
    portfolioBody = forms.CharField(widget=forms.Textarea)
    portfolioImg = forms.FileField()
    portfolioPub = forms.CharField(label='Hiển Thị', widget=forms.RadioSelect(choices=FRUIT_CHOICES))
    portfolioTimePub = forms.DateTimeField()
     
