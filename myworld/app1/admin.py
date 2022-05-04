from django.contrib import admin
from .models import contactModel
from .models import possForm

admin.site.register(contactModel)
# Register your models here.
admin.site.register(possForm)