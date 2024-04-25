from django.db import models

# Create your models here.

class tbl_localbodytype(models.Model):
    localbodytype_name = models.CharField(max_length=50)

class tbl_localbody(models.Model):
    localbodytype=models.ForeignKey(tbl_localbodytype,on_delete=models.CASCADE)    
    localbody= models.CharField(max_length=50)

class tbl_ward(models.Model):
    localbody=models.ForeignKey(tbl_localbody,on_delete=models.CASCADE)    
    ward= models.CharField(max_length=50)

class tbl_donationtype(models.Model):
    donationtype = models.CharField(max_length=50)    

class tbl_team(models.Model):
    team_name=models.CharField(max_length=50)
    member_count = models.CharField(max_length=50)   
     