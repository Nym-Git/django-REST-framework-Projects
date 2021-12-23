from django.db import models
from django.db.models import fields
from .models import Book,Author
from rest_framework import serializers

class bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class authorserializer(serializers.ModelSerializer):
    books = bookserializer(read_only=True,many=True)
    class Meta:
        model = Author
        fields = '__all__'