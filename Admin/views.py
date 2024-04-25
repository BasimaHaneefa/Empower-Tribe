from django.shortcuts import render,redirect
from Admin.models import *

# Create your views here.

def localbodytype(request):
    loc=tbl_localbodytype.objects.all()
    if request.method =="POST":
        tbl_localbodytype.objects.create(localbodytype_name=request.POST.get("txt_bodytype"))
        return redirect("Webadmin:localbodytype")
    else:
        return render(request,"Admin/Localbody_type.html",{"data":loc})

def editbodytype(request,id):
    editloc=tbl_localbodytype.objects.get(id=id)
    if request.method =="POST":
        editloc.localbodytype_name=request.POST.get("txt_bodytype")
        editloc.save()
        return redirect("Webadmin:localbodytype")
    else:
        return render(request,"Admin/Localbody_type.html",{"editloc":editloc})     

def delloctype(request,id):
    tbl_localbodytype.objects.get(id=id).delete()  
    return redirect("Webadmin:localbodytype")

def localbody(request):
    loc=tbl_localbodytype.objects.all()
    data=tbl_localbody.objects.all()
    if request.method == "POST":
        tbl_localbody.objects.create(localbodytype=tbl_localbodytype.objects.get(id=request.POST.get("sel_locbody")),
        localbody=request.POST.get("txt_locbody")
        )
        return redirect("Webadmin:localbody")
    else:    
        return render(request,"Admin/Localbody.html",{"loc":loc,"data":data})

def editloc(request,id):
    loc=tbl_localbodytype.objects.all()
    editdata=tbl_localbody.objects.get(id=id)
    if request.method == "POST":
        loc.localbodytype=tbl_localbodytype.objects.get(id=request.POST.get("sel_locbody")),
        editdata.localbody=request.POST.get("txt_locbody")
        editdata.save()
        return redirect("Webadmin:localbody")
    else:    
        return render(request,"Admin/Localbody.html",{"loc":loc,"editdata":editdata})


def delloc(request,id):
    tbl_localbody.objects.get(id=id).delete()  
    return redirect("Webadmin:localbody")        


def ward(request):
    loc=tbl_localbody.objects.all()
    data=tbl_ward.objects.all()
    if request.method == "POST":
        tbl_ward.objects.create(localbody=tbl_localbody.objects.get(id=request.POST.get("sel_locbody")),
        ward=request.POST.get("txt_ward")
        )
        return redirect("Webadmin:ward")
    else:    
        return render(request,"Admin/ward.html",{"loc":loc,"data":data})

def editward(request,id):
    loc=tbl_localbody.objects.all()
    editdata=tbl_ward.objects.get(id=id)
    if request.method == "POST":
        loc.localbody=tbl_localbody.objects.get(id=request.POST.get("sel_locbody")),
        editdata.ward=request.POST.get("txt_ward")
        editdata.save()
        return redirect("Webadmin:ward")
    else:    
        return render(request,"Admin/ward.html",{"loc":loc,"editdata":editdata})


def delward(request,id):
    tbl_ward.objects.get(id=id).delete()  
    return redirect("Webadmin:ward")        


def donation(request):
    loc=tbl_donationtype.objects.all()
    if request.method =="POST":
        tbl_donationtype.objects.create(donationtype=request.POST.get("txt_donation"))
        return redirect("Webadmin:donation")
    else:
        return render(request,"Admin/Donation_type.html",{"data":loc})

def editdonationtype(request,id):
    editloc=tbl_donationtype.objects.get(id=id)
    if request.method =="POST":
        editloc.donationtype=request.POST.get("txt_donation")
        editloc.save()
        return redirect("Webadmin:donation")
    else:
        return render(request,"Admin/Donation_type.html",{"editloc":editloc})     

def deldonationtype(request,id):
    tbl_donationtype.objects.get(id=id).delete()  
    return redirect("Webadmin:donation")


def team(request):
    team=tbl_team.objects.all()
    if request.method =="POST":
        tbl_team.objects.create(team_name=request.POST.get("txt_name"),member_count=request.POST.get("txt_count"))
        return redirect("Webadmin:team")
    else:
        return render(request,"Admin/Add_team.html",{"data":team})     


def editteam(request,id):
    team=tbl_team.objects.get(id=id)    
    if request.method=="POST":
        team.team_name=request.POST.get("txt_name")
        team.member_count=request.POST.get("txt_count")   
        team.save()
        return redirect("Webadmin:team") 
    else:
        return render(request,"Admin/Add_team.html",{"team":team})