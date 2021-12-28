from rest_framework import pagination
from rest_framework import permissions
from .serializers import bookserializer,authorserializer
from .models import Author, Book

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination ,LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend      #filters
from rest_framework import filters                                 # search filters

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


# nested-serializers using Genrics...
class AuthorVIEW(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = authorserializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated,DjangoModelPermissions]        # for restrict the user permision by admin/User permissions

class AuthorDetail_VIEW(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class = authorserializer




class booklistVIEW(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class = bookserializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]                      # for Django-Authantication

class bookdetails_VIEW(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class = bookserializer

