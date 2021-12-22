from django.db.models import query
from django.shortcuts import render
from .serializers import productSerializer
from .models import Item

from django.http import Http404
from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework import status

# Class genric based view
# non-primery-key based operations

class product_list(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = productSerializer


# Primery-key based all operation
class product_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = productSerializer