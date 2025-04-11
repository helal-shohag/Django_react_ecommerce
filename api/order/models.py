from django.db import models
from api.product.models import Product
from api.user.models import userModel
# Create your models here.


class OrderModel(models.Model):
    user = models.ForeignKey(userModel,on_delete=models.CASCADE,blank=True,null=True)
    product_names = models.CharField(max_length=200)
    total_products =models.CharField(max_length=500,default=0)
    total_amount = models.CharField(max_length=50,default=0)

    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
