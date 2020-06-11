from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class user(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone = PhoneNumberField()

    def __str__(self):
        return self.id
    