import email
from pyexpat import model
from django.db import models
from matplotlib.style import use


# --------------contact-------------
class contactModel(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email

# --------------postForm()-------------


class possForm(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
