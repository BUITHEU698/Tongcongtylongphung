from django import forms
from ..models import contacForm

class contacForm (forms.ModelForm):
    class Meta:
        model = contacForm
        fields = ['username', 'email','subject', 'message' ]