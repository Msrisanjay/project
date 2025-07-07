from django.urls import path
from .views import *

urlpatterns =[
     path('home/', homepage),
     path('contact/', contactpage),
     path('service/', servicepage),
     path('about/', aboutpage)
     
    
]