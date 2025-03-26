from django.urls import path,include
from .views import home

urlpatterns = [
    path('',home,name ='api.home'),
    path('category/', include('api.category.urls')),
    path('product/',include('api.product.urls')),
]