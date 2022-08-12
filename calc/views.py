from django import template
from django.core import paginator
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Allgroups,patient
from django.contrib.auth.models import User,auth
from .forms import PostForm,PostForm1,PostForm2
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages

# Create your views here.
def bloodgroups(request):
    ag=Allgroups.objects.all()
    template=loader.get_template('calc/bloodgroups.html')
    context={'ag':ag,}
    return HttpResponse(template.render(context))



def contact(request):
    ag=Allgroups.objects.all()
    template=loader.get_template('calc/contact.html')
    context={'ag':ag,}
    return HttpResponse(template.render(context))

def search(request):
    if  request.method =="POST":
        bloodgroup=request.POST.get("bloodgroup")
        bgsearchobj=Allgroups.objects.raw('select * from "calc_allgroups" where bloodgroup="'+bloodgroup+'"')
        return render(request,'calc/search.html',{"Allgroups":bgsearchobj})
    else:
       # bgobj=Allgroups.objects.raw('select * from "calc_allgroups"'){"Allgroups":bgobj}
        return render(request,'calc/search.html')


def bloodtips(request):
    return render(request,'calc/bloodtips.html')

def bloodfacts(request):
    return render(request,'calc/bloodfacts.html')

def donar(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        form.save()
        messages.info(request, 'Your details has been added successfully!')
        return render(request,"calc/donar.html",{"form":form})
    else:
        form=PostForm()    
        return render(request,"calc/donar.html",{"form":form})

 
def register(request):
    regForm=UserCreationForm
    if request.method=='POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request,'user has been registered.')
            return redirect('login')
    return render(request,'registration/register.html',{"form":regForm})


def home(request):
    return render(request,'calc/home.html')

def login(request):
    if request.method=='POST':
        form1=AuthenticationForm(data=request.POST)
        if form1.is_valid():
            return redirect('bloodgroups')
    else:
        form1=AuthenticationForm()
    return render(request,'registration/login.html',{'form':form1})

def logout(request):
    return render(request,'registration/logout.html')


def services(request):
    if request.method=="POST":
        form2=PostForm1(data=request.POST)
        form2.save()
        messages.info(request, 'Your feedback has been added successfully!')
        return render(request,"calc/services.html",{"form":form2})
    else:
        form2=PostForm1()    
    return render(request,"calc/services.html",{"form":form2})

def donarhome(request):
    return render(request,'calc/donarhome.html')

def patienthome(request):
    return render(request,'calc/patienthome.html')

def pservices(request):
    if request.method=="POST":
        form3=PostForm1(data=request.POST)
        form3.save()
        messages.info(request, 'Your feedback has been added successfully!')
        return render(request,"calc/pservices.html",{"form":form3})
    else:
        form3=PostForm1()    
    return render(request,"calc/pservices.html",{"form":form3})

def pregistration(request):
    form4=PostForm2(data=request.POST,files=request.FILES)
    if form4.is_valid():
        ins=form4.save()
        obj=form4.instance
        messages.info(request, 'Your details has been added successfully!')
        return render(request,"calc/pregistration.html",{"obj":obj})
    else:
        form4=PostForm2()
        img=patient.objects.all()    
        return render(request,"calc/pregistration.html",{"form":form4,"img":img})
    return render(request,"calc/pregistration.html",{"form":form4})

def dsearch(request):
    if  request.method =="POST":
        patientBloodGroup=request.POST.get("patientBloodGroup")
        bgsearchobj1=patient.objects.raw('select * from "calc_patient" where patientBloodGroup="'+patientBloodGroup+'"')
        return render(request,'calc/dsearch.html',{"patient":bgsearchobj1})
    else:
       # bgobj=Allgroups.objects.raw('select * from "calc_allgroups"'){"Allgroups":bgobj}
        return render(request,'calc/dsearch.html')    