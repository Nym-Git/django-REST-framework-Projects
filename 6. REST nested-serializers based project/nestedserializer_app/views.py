from .serializers import bookserializer,authorserializer
from .models import Author, Book

from rest_framework.views import APIView
from rest_framework import generics


# nested-serializers using Genrics...
class AuthorVIEW(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = authorserializer

class AuthorDetail_VIEW(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class = authorserializer

class booklistVIEW(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class = bookserializer

class bookdetails_VIEW(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class = bookserializer