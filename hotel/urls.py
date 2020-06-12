from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel, name='hotel'),
    path('hotelAdd/', views.hotelAdd, name='hotelAdd'),
]