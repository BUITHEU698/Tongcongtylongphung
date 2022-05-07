from django import forms


# --------------contact-------------
class contactForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


# # --------------memberForm-------------

# class memberForm(forms.Form):
#     username = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length = 30)
#     # phone = forms.CharField(max_length=11)
#     password = forms.CharField(max_length=20, widget = forms.PasswordInput)
# # --------------memberForm-------------


# class loginForm(forms.Form):
#     username = forms.CharField(max_length=30)
#     password = forms.CharField(max_length=20, widget=forms.PasswordInput)
