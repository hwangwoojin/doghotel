from django.urls import path
from . import views

urlpatterns = [
    path('mypage/', views.mypage, name='mypage'),
    path('mydog/', views.mydog, name='mydog'),
]