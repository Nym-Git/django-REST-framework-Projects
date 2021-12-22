from django.urls import path, include
from .import views

urlpatterns = [
    path('product/',views.product_list.as_view()),
    path('product/<int:pk>',views.product_details.as_view()), 
]
