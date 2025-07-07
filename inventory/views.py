from django.shortcuts import render

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
