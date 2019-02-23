from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=200)
    isHeABitch = models.BooleanField()

    def __str__(self):
        return self.user.username
