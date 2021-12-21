from django.http.response import Http404
from django.shortcuts import render
from .models import item
from .serializers import productSerializer

from rest_framework.response import Response 
from rest_framework import serializers, status
from rest_framework.views import APIView

# Class based "VIEWS"
class product_GET_POST(APIView):

    def get(self,request):
        products = item.objects.all()
        serializer = productSerializer(products)
        return Response(serializer.data)
   
    def post(self,request):
        serializer = productSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class product_get_PUT_Delete(APIView):
    
    def get_object(self,pk):
        try:
            return item.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk):
        product_object = self.get_object(pk)
        serializer = productSerializer(product_object)
        return Response(serializer.data)

    def put(self,request,pk):
        product_object = self.get_object(pk)
        serializer = productSerializer(product_object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        product_object = self.get_object(pk)
        product_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        


