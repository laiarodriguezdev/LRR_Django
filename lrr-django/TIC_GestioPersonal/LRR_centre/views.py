from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    professor = {"nom": "Oriol", "cognom": "Roca", "edat": 25}
    return render(request, 'home.html', {'professor': professor})