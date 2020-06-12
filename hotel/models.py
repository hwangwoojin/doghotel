from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class hotels(models.Model):
    name = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    homepage = models.CharField(max_length=50, blank=True)
    phone = PhoneNumberField(blank=True)
    rate = models.FloatField(default=0, blank=True)

    def __str__(self):
        return str(self.name)
