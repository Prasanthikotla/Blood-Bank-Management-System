from django.core import validators
from django.db import models
from django.db.models import constraints
from django.db.models import fields
from django.db.models.fields import IntegerField

# Create your models here.
class Allgroups(models.Model):
    donarname=models.CharField(max_length=200)
    bloodgroup=models.CharField(max_length=100)
    dob=models.CharField(max_length=20)
    place=models.CharField(max_length=50)
    mobile=models.IntegerField()
    mail_id=models.EmailField(max_length=50)
    def __str__(self):
        return self.donarname
    class Meta:
        db_table="calc_allgroups"
   

class Services(models.Model):
    Name=models.CharField(max_length=200)
    PhoneNumber=models.IntegerField()
    Email=models.EmailField(max_length=50)
    Comments=models.CharField(max_length=200)
    def __str__(self):
        return self.Name
    class Meta:
        db_table="calc_services"

class patient(models.Model):
    patientName=models.CharField(max_length=200)
    address=models.CharField(max_length=250)
    patientBloodGroup=models.CharField(max_length=4)
    hospitalName=models.CharField(max_length=200)
    mobileNumber=models.IntegerField()
    image=models.ImageField(upload_to="img/%y")
    age=models.IntegerField()
    def __str__(self):
        return self.patientName
    class Meta:
        db_table="calc_patient"

    
