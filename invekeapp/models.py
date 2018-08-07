from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Business(models.Model):
    investidea=models.CharField(max_length=51)
    post = HTMLField(blank=False)
    locationjpg=models.ImageField(upload_to = 'jpg/')
