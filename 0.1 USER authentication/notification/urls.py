from django import views
from django.urls import path,include
from .import views

urlpatterns = [
 path('phone_otp/', views.phone_otp, name='phone_otp'),
]
