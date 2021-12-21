from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Item

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields=['id','product_name','product_dicpriction','product_visibility','Product_rate']