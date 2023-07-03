from .views import *
from django.urls import path,include
from django.contrib.auth import views 


urlpatterns = [
    path('', login,name='login'),
    path('signup',signup,name='signup'),
    path('logout',logout,name='logout'),
    
]
