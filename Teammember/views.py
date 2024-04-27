from django.shortcuts import render,redirect
from Teammember.models import *

# Create your views here.

def homepage(request):
    return render(request,"Teammember/Homepage.html")


def family(request):
    data=tbl_family.objects.filter(teammember=tbl_teammember.objects.get(id=request.session["mid"]))
    if request.method == "POST":
        tbl_family.objects.create(teammember=tbl_teammember.objects.get(id=request.session["mid"]),
        family_housename=request.POST.get("txt_housename"),
        family_address=request.POST.get("txt_address"),
        )
        return redirect("Webteammember:family")
    else:
        return render(request,"Teammember/Add_family.html",{"data":data})
    
def familymembers(request,id):  
    data=tbl_familymember.objects.filter(family=tbl_family.objects.get(id=id))
    if request.method == "POST":
        tbl_familymember.objects.create(family=tbl_family.objects.get(id=id),
        family_member_counter=request.POST.get("txt_count"),
        family_member_name=request.POST.get("txt_name"),
        family_member_relation=request.POST.get("txt_relation"),
        family_member_age=request.POST.get("txt_age"),
        family_member_gender=request.POST.get("Gender"))
        return redirect("Webteammember:family")
    else:
        return render(request,"Teammember/Add_Familymembers.html",{"data":data})
    

def Product(request,id):
    category=tbl_category.objects.all()
    if request.method=="POST":
        tbl_product.objects.create(product_name=request.POST.get("txtname"),
                                  product_price=request.POST.get("txtprice"),
                                  product_details=request.POST.get("txtdetails"),
                                  product_stock=request.POST.get("txtstock"),
                                  product_category=tbl_category.objects.get(id=request.POST.get("sel_category")),
                                  family=tbl_family.objects.get(id=id),
                                  member=tbl_teammember.objects.get(id=request.session["mid"]),
                                  product_image=request.FILES.get("pimage")
                                       )
        return redirect("Webteammember:family")
    else:
        return render(request,"Teammember/Add_Products.html",{'data':category})    
    

def viewproduct(request):
    data=tbl_product.objects.filter(member=tbl_teammember.objects.get(id=request.session["mid"]))
    return render(request,"Teammember/ViewProducts.html",{"data":data})
                        