from django.urls import path
from .views import *

urlpatterns =[
     path('home/', homepage),
     path('contact/', contactpage),
     path('service/', servicepage),
     path('about/', aboutpage),
     path('product/add/',productadd),
     path('products/',Allproducts),
     path('products/delete/<int:id>',deleteproducts,name='product_delete'),
     path('products/update/<int:id>',productupdate,name='product_update'),
    
]