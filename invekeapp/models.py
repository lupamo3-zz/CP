from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Business(models.Model):
    investidea=models.CharField(max_length=51)
    post = HTMLField(blank=False)
    locationjpg=models.ImageField(upload_to = 'jpg/')
    pub_date=models.DateField(null=True, blank=True)

    def __str__(self):
        return self.investidea

    class Meta:
        ordering=['investidea']


    def save_locationjpg(self):
        self.save()

    def delete_locationjpg(self):
        self.delete()

    @classmethod
    def get_all(cls):
        locationjpg=cls.objects.order_by('-pub_date')
        return locationjpg

class Faq(models.Model):
    faq=
