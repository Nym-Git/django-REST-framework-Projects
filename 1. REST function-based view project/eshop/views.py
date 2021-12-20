from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import productSerializers
from eshop.models import product


@api_view(['GET','POST'])
def productVIEW(request):
    
    if request.method == 'GET':
        productLIST = product.objects.all()
        serializer = productSerializers(productLIST,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = productSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def product_detailVIEW(request,pk):
    try:
        product_Data = product.objects.get(pk=pk)
    except product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = productSerializers(product_Data)
        return Response(serializer.data)

#   Update the data
    elif request.method == 'PUT':
        serializer = productSerializers(product,data=request.data)
        if serializers.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUESTS)
        
#   delete the data
    elif request.mehtod == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)























'''
def productVIEW(request):
    item={
        'id': 123,
        'product_name': 'Tshirt',
        'product_visibility': 12,
        'Product_rate': 32, 
    }
    
    data = product.objects.all()
    response = {'product':list(data.values('product_name','Product_rate'))}
    
    return JsonResponse(response)'''