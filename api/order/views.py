from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from .models import OrderModel
from rest_framework import viewsets
from serializers import OrderSerializers
 
# Create your views here.


def validate_user_session(id, token):
    UserModel = get_user_model()

    try:
        pass
    except expression as identifier:
        pass