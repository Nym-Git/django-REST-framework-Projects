from django.urls import include, path
from .import views

urlpatterns = [
    path('email/', views.parameter, name='email'),
]
