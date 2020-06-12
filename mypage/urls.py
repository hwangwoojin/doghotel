from django.urls import path
from . import views

urlpatterns = [
    path('mypage/', views.mypage, name='mypage'),
    path('mydog/', views.mydog, name='mydog'),
    path('mydog/add', views.mydogAdd, name='mydogAdd'),
    path('', views.hotel, name='hotel'),
    path('hotelAdd/', views.hotelAdd, name='hotelAdd'),
    path('hotelRate/', views.hotelRate, name='hotelRate'),
    path('hotelNameSearch/', views.hotelNameSearch, name='hotelNameSearch'),
    path('hotelLocationSearch/', views.hotelLocationSearch, name='hotelLocationSearch'),
]