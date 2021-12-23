from rest_framework import pagination
from .serializers import bookserializer,authorserializer
from .models import Author, Book

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination ,LimitOffsetPagination

# overwrite on page-pagination limits
class AuthorPagination(PageNumberPagination):
    page_size=2


# nested-serializers using Genrics...
class AuthorVIEW(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = authorserializer
    pagination_class = AuthorPagination          # calling the local-pagination

class AuthorDetail_VIEW(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class = authorserializer

class booklistVIEW(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class = bookserializer
    pagination_class = LimitOffsetPagination     # diffrent thing (by WEB-url)

class bookdetails_VIEW(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class = bookserializer