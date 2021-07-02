from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField

class Profile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    