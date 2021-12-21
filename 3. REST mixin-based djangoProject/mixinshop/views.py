from django.shortcuts import render
from .serializers import productSerializer 
from .models import Item

from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework.response import Response


# Class based view using genrics
class product_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = productSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)


# primery key based operation 
class product_list_operation(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = productSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)


    