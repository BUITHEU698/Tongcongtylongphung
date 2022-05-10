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
