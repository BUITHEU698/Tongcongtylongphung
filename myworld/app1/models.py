
import email
from pyexpat import model
from django.db import models
from django.urls import reverse
from matplotlib.style import use


# --------------contact-------------
class contactModel(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email

# --------------postBlog-------------
class postBlog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail',args=[self.id,])
