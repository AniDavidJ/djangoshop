from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})

def about(request):
    return HttpResponse("<h1>About Page</h1>")

def contact(request):
    return HttpResponse("<h1>Contact Us.....</h1>")