from django.db import models
from django.contrib.auth.models import User


class CustomerSignUp(models.Model):
    user = models.OneToOneField(
        User, unique=True, on_delete=models.CASCADE, related_name='customer')
    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    address = models.CharField(
        max_length=250, default='Addis Ababa,Ethiopia', blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile', blank=True, null=True)
    designation = models.CharField(max_length=100, blank=False)
    phone = models.IntegerField(max_length=15, blank=True, null=True)
    information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


# class CustomerLogin(models.Model):
#     username = models.CharField(max_length=250, blank=False, null=False)
#     password = models.PasswordField(max_length=100, blank=False)