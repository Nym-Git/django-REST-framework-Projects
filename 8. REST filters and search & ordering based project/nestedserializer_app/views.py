from rest_framework import pagination
from .serializers import bookserializer,authorserializer
from .models import Author, Book

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination ,LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend      #filters
from rest_framework import filters                                 # search filters

# overwrite on page-pagination limits
class AuthorPagination(PageNumberPagination):
    page_size=2


# nested-serializers using Genrics...
class AuthorVIEW(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = authorserializer
    filter_backends = [DjangoFilterBackend]               #   filters
    filterset_fields = ['first_name','last_name']         #   filters

class AuthorDetail_VIEW(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class = authorserializer

class booklistVIEW(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class = bookserializer
    filter_backends = [filters.SearchFilter]               #   search filter
    search_fields = ['book_name','^ratings',]              #   search filter


class bookdetails_VIEW(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class = bookserializer


class Ordering_EXAMPLE_view(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = bookserializer
    filter_backends = [filters.OrderingFilter]               # Ordering filter
    ordering_fields = ['ratings']
    ordering = ['-id']                                       # descending order
