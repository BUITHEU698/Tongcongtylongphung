from django import forms



#--------------contact-------------
class contactForm(forms.Form):
    username = forms.CharField(max_length= 25)
    email = forms.EmailField()
    subject = forms.CharField(max_length= 100)
    message = forms.CharField(widget= forms.Textarea)
    
    
    
    
#--------------contact-------------