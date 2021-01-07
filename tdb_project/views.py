from django.shortcuts import render, HttpResponse
from django.contrib import messages
# Create your views here.
from django.shortcuts import render
from .models import CareersOpportunity, Teams, Applicant


def index(request):
    return render(request, 'index.html')


def company(request):
    return render(request,'test.html')


def career(request):
    careerData = CareersOpportunity.objects.all()
    return render(request, 'careers.html', {"data": careerData})


def team(request):
    teamData = Teams.objects.all()
    mediadata=Applicant.objects.all()
    return render(request, 'team.html', {'teamData': teamData,'mediadata':mediadata})


def basic(request):
    return render(request,'basic.html')


def contact(request):
    return render(request,'contact.html')


def product(request):
    return render(request,'product1.html')


def applicant(request):
    return render(request,'form.html')

def submit(request):
    fname=request.POST['first_name']
    lname=request.POST['last_name']
    remail=request.POST['email']
    rphone=request.POST['phone']
    rresume=request.FILES['resume']
    submitdata=Applicant(name=fname,lastName=lname,email=remail,phone=rphone,resume=rresume)
    submitdata.save()
    return render(request,'company.html',{'message':'Form submitted successfully'})