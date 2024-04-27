from django.shortcuts import render
from Teammember.models import *
# Create your views here.

def homepage(request):
    return render(request,"User/Homepage.html")

def viewproduct(request):
    data=tbl_product.objects.all()
    return render(request,"User/ViewProducts.html",{"data":data})