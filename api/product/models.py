from django.db import models
from api.category.models import Category


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    decription = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    price = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True,blank=True)
    image= models.ImageField(upload_to= 'images/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.name
   
        