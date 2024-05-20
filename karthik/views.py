from django.shortcuts import render

# Create your views here.


def home(request):

    return render(request,'index.html')

def about(request):

    return render(request,'about.html')

def service(request):

    return render(request,'service.html')

def project(request):
    return render(request,'project.html')

def skill(request):
    return render(request,'skill.html')

def contact(request):
    return render(request,'contact.html')