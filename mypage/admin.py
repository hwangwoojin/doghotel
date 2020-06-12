from django.contrib import admin
from .models import user, dog, hotels, reservations
# Register your models here.

admin.site.register(user)
admin.site.register(dog)
admin.site.register(hotels)
admin.site.register(reservations)