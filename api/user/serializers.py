from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes ,permission_classes
from .models import userModel

class userSerializers(serializers.HyperlinkedModelSerializer):

    def create(self,validated_data,):
        password = validated_data.pop('password',None)
        instance =self.meta.model(** validated_data)
        instance.save()
        return instance
    
        if password is not None:
          instance.set_password(password)

    def update(self,instance,validated_data):
        for attr,value in validated_data.items():
            if attr == 'password':
                instance.set_password()

            else:
                setattr(instance,attr,value)

        instance.save()
        return instance
        
    class meta:
        model = userModel
        extra_kwargs = {'password' : {'write_only':True}}
        fields = ('name','email','phone','gender','session_token','is_active','is_staff','is_superuser')
        