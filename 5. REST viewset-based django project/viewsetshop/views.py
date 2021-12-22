from django.shortcuts import render
from django.http import Http404
from .serializers import productSerializer
from .models import Item

from rest_framework.views import APIView
from rest_framework import generics,mixins, serializers
from rest_framework import viewsets


# model-view-set      {all operation:- primery-key based and non-primery key based}    ReadOnlyModelViewSet...
class product_CRUD(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = productSerializer
