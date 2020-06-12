from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel, name='hotel'),
    path('hotelAdd/', views.hotelAdd, name='hotelAdd'),
    path('hotelRate/', views.hotelRate, name='hotelRate'),
    path('hotelNameSearch/', views.hotelNameSearch, name='hotelNameSearch'),
    path('hotelLocationSearch/', views.hotelLocationSearch, name='hotelLocationSearch'),
]