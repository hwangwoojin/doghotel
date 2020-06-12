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
    feature = models.CharField(max_length=140, blank=True)
    userid = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.userid)

class hotels(models.Model):
    name = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    homepage = models.CharField(max_length=50, blank=True)
    phone = PhoneNumberField(blank=True)
    rate = models.FloatField(default=0, blank=True)
    userid = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class reservation(models.Model):
    managerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)