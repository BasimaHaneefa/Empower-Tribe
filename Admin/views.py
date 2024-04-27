from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
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

def Assign(request,id):
    ward=tbl_ward.objects.all()
    if request.method =="POST":
        tbl_assigmment.objects.create(team=tbl_team.objects.get(id=id),ward=tbl_ward.objects.get(id=request.POST.get("sel_ward")))
        return redirect("Webadmin:team")
    else:
        return render(request,"Admin/Assignteam.html",{"data":ward})

def editteam(request,id):
    team=tbl_team.objects.get(id=id)    
    if request.method=="POST":
        team.team_name=request.POST.get("txt_name")
        team.member_count=request.POST.get("txt_count")   
        team.save()
        return redirect("Webadmin:team") 
    else:
        return render(request,"Admin/Add_team.html",{"team":team})
    

def delteam(request,id):
    tbl_team.objects.get(id=id).delete()
    return redirect("Webadmin:team")


def MemberRegistration(request,id):
    memberdata=tbl_teammember.objects.all()
    if request.method=="POST":
      tbl_teammember.objects.create(member_name=request.POST.get('txtname'),
                                       member_contact=request.POST.get('txtnumber'),
                                       member_email=request.POST.get('txtemail'),
                                       member_address=request.POST.get('txtaddress'),
                                       member_photo=request.FILES.get('Photo'),
                                       member_proof=request.POST.get('Proof'),
                                       member_password=request.POST.get('txtpassword1'),
                                       assignment=tbl_assigmment.objects.get(id=id)
                                       )
      return render(request,"Admin/Add_members.html",{memberdata:memberdata})
    else:
      return render(request,"Admin/Add_members.html",{memberdata:memberdata})
    
def AssignedTeams(request):
    team=tbl_assigmment.objects.all()
    return render(request,"Admin/Assigned_teams.html",{"data":team})


def category(request):
    loc=tbl_category.objects.all()
    if request.method =="POST":
        tbl_category.objects.create(category_name=request.POST.get("txt_category"))
        return redirect("Webadmin:category")
    else:
        return render(request,"Admin/Category.html",{"data":loc})

def editcat(request,id):
    editloc=tbl_category.objects.get(id=id)
    if request.method =="POST":
        editloc.category_name=request.POST.get("txt_category")
        editloc.save()
        return redirect("Webadmin:category")
    else:
        return render(request,"Admin/Category.html",{"editloc":editloc})     

def delcat(request,id):
    tbl_category.objects.get(id=id).delete()  
    return redirect("Webadmin:category")


def Registration(request):
    regdata=tbl_registration.objects.all()
    if request.method=="POST":
       tbl_registration.objects.create(registration_name=request.POST.get("txtname"),
                                       registration_contact=request.POST.get("txtnumber"),
                                       registration_email=request.POST.get("txtemail"),
                                       registration_password=request.POST.get("txtpassword")
                                       )
       return render(request,"Admin/Registration.html",{'reg':regdata})
    else:
       return render(request,"Admin/Registration.html",{'reg':regdata}) 

def delreg(request,did):
    tbl_registration.objects.get(id=did).delete() 
    return redirect("Webadmin:registration") 




def ViewComplaint(request):
    newcom=tbl_complaint.objects.filter(complaint_status=0)
    recom=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,"Admin/ViewComplaint.html",{'new':newcom,'repl':recom})
  
def Reply(request,rid):
    com=tbl_complaint.objects.get(id=rid)
    if request.method=="POST":
        com.complaint_reply=request.POST.get("txtpro")
        com.complaint_status=1
        com.save()
        return redirect("webadmin:ViewComplaint")
    else:
        return render(request,"Admin/Reply.html")
    
def ViewFeedback(request):
    data=tbl_feedback.objects.all()
    return render(request,"Admin/ViewFeedback.html",{'data':data})   