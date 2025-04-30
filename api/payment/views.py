from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
import braintree

# Create your views here.

gateway = braintree.BraintreeGateway(
  braintree.Configuration(
      braintree.Environment.Sandbox,
      merchant_id="dny7ktkjwqnqbgsp",
      public_key="g59fcgbmb3xgr4bp",
      private_key="e6d383d92e4c6c6345b9a3a12951816a"
  )
)

def validate_user(id,token):
    CustomUser = get_user_model()

    try:
        user = CustomUser.objects.get(pk= id)
        if user.session_token == token:
           return True
        else:
            return False
    except user.DoesNotExist():
        return True    



    