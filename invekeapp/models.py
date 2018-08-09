from django.db import models
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
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

    FAQ=(
    ('salaries', 'Salaries and Wages'),
    ('corporate taxes','Corporate Taxes'),
    ('Education', 'Education'),
)
    faq=models.CharField(max_length=6, choices=FAQ)
    singlea=HTMLField(blank=False, default=False)
    image=models.ImageField(upload_to='img/')
    

    def __str__(self):
        return self.singlea

    class Meta:
        ordering=['singlea']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_all(cls):
        image=cls.objects.order_by('-singlea')
        return image



class Opportunity(models.Model):
    opportunity=models.CharField(max_length=30)

class News(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    pubdat = models.DateField(blank=True)



class Entry(models.Model):
    DRAFT = 'D'
    HIDDEN = 'H'
    PUBLISHED = 'P'
    ENTRY_STATUS = (
        (DRAFT, 'Draft'),
        (HIDDEN, 'Hidden'),
        (PUBLISHED, 'Published'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=4000, null=True, blank=True)
    summary = models.TextField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=10, choices=ENTRY_STATUS)
    start_publication = models.DateTimeField()
    created_by = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    edited_by = models.ForeignKey(User, null=True, blank=True, related_name="+")

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title

    @classmethod
    def get_all(cls):
        image=cls.objects.order_by('-title')
        return image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    # if created:
    #     Profile.objects.create(user=instance)
    # instance.profile.save()

    def __str__(self):
        return self.birth_date