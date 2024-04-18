from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    professor = {"nom": "Oscar", "cognom": "Rovira", "edat": 30}
    return render(request, 'index.html', {'professor': professor})

def student(request):
    alumnat = {"nom": "Oscar", "cognom": "Rovira", "edat": 30}
    return render(request, 'student.html', {'alumnat': alumnat})

def teacher(request):
    professor = {"nom": "Oscar", "cognom": "Rovira", "edat": 30}
    return render(request, 'teacher.html', {'professor': professor})