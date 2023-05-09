from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='user/', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    locality = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, null=True)
    mobile = models.IntegerField(default=0, null=True)
    zipcode = models.IntegerField(null=True)
    state = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


