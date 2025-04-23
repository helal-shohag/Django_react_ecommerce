from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from .models import OrderModel
from rest_framework import viewsets
from .serializers import OrderSerializers
 
# Create your views here.

def validate_user_session(id,token):
   UserModel =get_user_model()

   try:
      user = UserModel.objects.get(pk= id)
      if user.session_token == token:
         return True
      return False
   
   except UserModel.DoesNotExist:
      return False  
   

@csrf_exempt

def add(request,id,token):
   if not validate_user_session(id,token):
      return JsonResponse({'error': 'please re login'})
   if request.method == 'POST':
      user_id = request.POST('transaction_id')
      amount  = request.POST('amount')
      products = request.POST('products')
      
      total_pro = len(products.split(',')[:-1])

      UserModel =get_user_model()

      try:
          user = UserModel.objects.get(pk = user_id)
            
      except UserModel.DoesNotExist:
          return JsonResponse({'error': 'user does not exist'})

      order = OrderModel(user = user,transaction = user_id,total_product =total_pro,amount= amount,products =products)
      order.save()
      return JsonResponse({'success': 'order created Successfully'})    
   
class OrderViewSet(viewsets.ModelViewSet):
   queryset = OrderModel.objects.all().order_by('created_at')
   serializer_class = OrderSerializers