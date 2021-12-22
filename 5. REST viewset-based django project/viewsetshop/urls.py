from django.urls import path, include
from rest_framework import routers
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product',views.product_CRUD)


urlpatterns = [
    path('',include(router.urls)),
]
