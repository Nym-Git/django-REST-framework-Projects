from django.urls import path, include
from .import views

urlpatterns = [
    path('product/',views.product_GET_POST.as_view()),
    path('product/<int:pk>',views.product_get_PUT_Delete.as_view()), 
]
