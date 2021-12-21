from django.db import models

# Create your models here.
class Item(models.Model):
    product_name = models.CharField(max_length=100,blank=True)
    product_dicpriction = models.CharField(max_length=100,blank=True)
    product_visibility = models.IntegerField(blank=False,default=1)
    Product_rate = models.IntegerField(blank=False,default=1)

    def __str__(self):
        return self.product_name
        