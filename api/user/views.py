from django.shortcuts import render
from .models import  userModel
from .serializers import userSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout


import random
import re

def generate_session_token(length = 10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(length ))
@csrf_exempt
def SignUp(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a Post request with valid params'})
    
    username = request.POST['email']
    password = request.POST['password']

    if not re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b',username):
        return JsonResponse({'error': 'Email is not valid'})
    
    if len(password) < 3:
        return JsonResponse({'error': 'password needs to be at least 3 character'})
    

    UserModel = get_user_model

    try:
        user = UserModel.objects.get(email = username)
        if user.check_password(password):
            user_dict = UserModel.objects.filter(email =username).values().first()
            user_dict.pop('password')
            if user.session_token != '0':
                user.session_token = '0'
                user.save()
                return JsonResponse({'error': 'previeous session exist'})    
            
            token = generate_session_token()
            user.session_token = token 
            user.save()
            login(request, user)

            return JsonResponse({'token ': token,'user': user_dict})
        else:
            return JsonResponse({'error': 'invalid  Password'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'invalid Email'})
    
def SignOut(request,id):
    logout(get_user_model)    
    
class UserViewset(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = userModel.objects.all().order_by('id')
    serializer_class = userSerializer

    def get_permissions(self):
        try:
            return [permission() for  permission in self.permission_classes]
        except KeyError:
            return [permission() for permission in self.permission_classes]