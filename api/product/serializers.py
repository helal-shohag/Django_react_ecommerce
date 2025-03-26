from rest_framework import serializers
from .models import Product



class ProductSerializers(serializers.HyperlinkedModelSerializer):
   image = serializers.ImageField(max_length =None,allow_empty_file = False)
   class Meta:
      model = Product
      Fields = ("name","decription","category","stock",'image')