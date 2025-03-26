from django.http import JsonResponse


# Create your views here.

def home(request):
    return JsonResponse({'name':'Helal Uddin','About': 'JsonResponse'})


