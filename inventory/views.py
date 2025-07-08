from django.shortcuts import render , redirect
from .forms import *
from .models import *

# Create your views here.
def homepage(request):

    context = {
        "name" : "sri sanjay",
        "age" : 23,
        "role":"super"
    }



    return render(request,'index.html',context)

def contactpage(request):

    return render(request,'contact.html')

def aboutpage(request):

    return render(request,'about.html')

def servicepage(request):

    return render(request,'service.html')

def productadd(request):

    context = {
        'product_page': product_form()
    }

    if request.method == "POST":

        product_Form = product_form (request.POST)
        if product_Form.is_valid():

            product_Form.save()
        
    return render(request,'productadd.html',context)


def Allproducts(request):
    all_product = product.objects.all()
    return render(request,'products.html',{'all_product':all_product})

def deleteproducts(request , id):
    selected_product = product.objects.get(id = id)
    selected_product.delete()
    return redirect('/inventory/products/')

def productupdate(request, id):
     
     selected_product = product.objects.get(id = id)
     
     context = {
         
        'product_page' : product_form(instance=selected_product)

     }  

     if request.method == 'POST':
         product_Form = product_form (request.POST,instance=selected_product)
         if product_Form.is_valid():
             product_Form.save()
             return redirect('/inventory/products/')
         
     return render(request,'productadd.html',context)



    
     
