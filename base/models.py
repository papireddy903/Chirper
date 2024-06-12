from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings 

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True)
    profile_photo = models.ImageField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)

    @property 
    def Photourl(self):
        try: 
            url = self.profile_photo.url 
        except:
            url = settings.MEDIA_URL + 'default_img.jpg'
        return url 

 

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


    

class Chirp(models.Model):
    chirp = models.TextField(max_length=1000, blank=True, null=True) 
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.chirp}"
    

class Like(models.Model):
    chirp = models.ForeignKey(Chirp, on_delete=models.CASCADE) 
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.chirp} - {self.author}" 
    


