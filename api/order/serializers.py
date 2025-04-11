from rest_framework import serializers
from .models import OrderModel


class OrderSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderModel
        fileds = ('user')
