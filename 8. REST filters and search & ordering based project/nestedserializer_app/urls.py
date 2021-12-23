from django.urls import path, include
from rest_framework import routers, viewsets
from .import views

urlpatterns = [
    path('author/',views.AuthorVIEW.as_view()),
    path('author/<int:pk>/detail',views.AuthorDetail_VIEW.as_view()),
    path('ordering/',views.Ordering_EXAMPLE_view.as_view()),
    path('book/',views.booklistVIEW.as_view()),
    path('book/<int:pk>/detail',views.bookdetails_VIEW.as_view())
]
