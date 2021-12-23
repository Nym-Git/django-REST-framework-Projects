from django.db import models

# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)

class Book(models.Model):
    book_name=models.CharField(max_length=300)
    ratings=models.IntegerField(max_length=10)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)