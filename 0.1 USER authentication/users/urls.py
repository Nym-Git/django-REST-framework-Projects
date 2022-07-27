from django import views
from django.urls import path,include
from .import views

urlpatterns = [
 path('signup/', views.user_register ),
 path('signin/', views.login),
]
