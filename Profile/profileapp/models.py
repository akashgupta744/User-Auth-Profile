from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField (User, on_delete = models.CASCADE)

    name = models.CharField(default = 'Full Name (default)', max_length = 100, blank = True, null =True, )

    title = models.CharField(default = 'This is the default, title change it in profile', max_length = 100, blank = True, null =True)

    desc = models.TextField(null = True, blank = True, default='Hey, there this is a default text description about you that you can change on after clicking on "Edit"')

    profile_img = models.ImageField(upload_to='media', blank = True, null =True, default= 'media/default.jpg')

    phone_no = models.CharField(default = '98765 98765',  max_length = 10, validators = [MinLengthValidator(10)], blank = True, null =True)


    def __str__(self):
        return self.user.username