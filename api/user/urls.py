from rest_framework import routers
from django.urls import path,include
from . import views

router = routers.DefaultRouter()

router.register(r'',views.UserViewset)

urlpatterns = [
    path('signup/',views.SignUp,name='signup'),
    path('logout/<int:id>/',views.SignOut,name='signout'),
    path('',include(router.urls)),
    
]
