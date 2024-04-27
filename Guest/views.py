from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *

# Create your views here.
def Login(request):
    if request.method=="POST":
       login_email=request.POST.get("txtemail")
       login_password=request.POST.get("txtpassword")

       membercount = tbl_teammember.objects.filter(member_email=login_email,member_password=login_password).count() 
       usercount = tbl_userreg.objects.filter(userregistration_email=login_email,userregistration_password=login_password).count() 
       
       if membercount > 0:
          member = tbl_teammember.objects.get(member_email=login_email,member_password=login_password)
          request.session["mid"] = member.id
          return redirect("Webteammember:homepage")
       elif usercount > 0:
          user = tbl_userreg.objects.get(userregistration_email=login_email,userregistration_password=login_password)
          request.session["uid"] = user.id
          return redirect("Webuser:homepage")  
    else:                                           
        return render(request,"Guest/Login.html",{"msg":"error"})
    

def UserRegistration(request):
    if request.method=="POST":
      
      tbl_userreg.objects.create(userregistration_name=request.POST.get('txtname'),
                                       userregistration_contact=request.POST.get('txtnumber'),
                                       userregistration_email=request.POST.get('txtemail'),
                                       userregistration_address=request.POST.get('txtaddress'),
                                       userregistration_photo=request.FILES.get('Photo'),
                                       userregistration_password=request.POST.get('txtpassword'),
                                       userregistration_proof=request.POST.get('Proof')
                                       )
      return render(request,"Guest/UserRegistration.html")
    else:
      return render(request,"Guest/UserRegistration.html")    