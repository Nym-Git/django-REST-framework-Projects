from django.urls import path
from .import views

urlpatterns = [
    path('product/', views.productVIEW,name='product'),
    path('product-Details/<int:pk>', views.product_detailVIEW,name='product_details'),
    path('<int:pk>/product-CRUD', views.product_detailVIEW,name='product_CRUD'),
]
