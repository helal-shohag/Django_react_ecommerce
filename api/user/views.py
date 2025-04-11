from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import login,logout
from rest_framework.permissions import AllowAny
from .serializers import userSerializers
from .models import userModel
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
import random
import re
# Create your views here.

def generate_session_token(length= 10):    
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(length))

def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'your Request doesnot exist'})


    username = request.POST('email')
    password = request.POST('password')

    if not  re.match("^[\w\.\+\-]+\@[\w+\.[a-z]{2,3$}",username):
        return JsonResponse({'error': 'Enter a valid email'})
        

    if len(password) < 3:
        return JsonResponse({'error': 'password Must be at least 3 chaarecter'})    