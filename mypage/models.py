from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class user(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone = PhoneNumberField(blank=True)

    def __str__(self):
        return str(self.id)

class dog(models.Model):
    name = models.CharField(max_length=50, blank=True)
    breed = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(default=0, blank=True)
    weight = models.IntegerField(default=0, blank=True)
    userid = models.ForeignKey(user, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)