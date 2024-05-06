from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .form import PersonaFrom
from .models import Usuari

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    professor = {"nom": "Oscar", "cognom": "Rovira", "edat": 30}
    return render(request, 'index.html', {'professor': professor})

def user_form(request):
    form = PersonaFrom(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {'form': form }
    return render(request, 'form.html', context)

def student(request):
    # alumnes = [
    #     {'nom': 'Laia', 'cognom': 'Rodríguez',  'rol': 'Estudiant', 'link':'+INFO'},
    #     {'nom': 'Harpreet', 'cognom': 'Kaur', 'rol': 'Estudiant',  'link':'+INFO'}
    # ]
    alumnes = Usuari.objects.filter(rol__nom='alumne') #AQUI TINC ALGO QUE NO ESTÁ REFINAT.
    context = {'alumnes': alumnes}    
    return render(request, 'student.html', context)

def teacher(request):
    # teachers = [
    #     {'nom': 'Oscar', 'cognom': 'Rovira', 'edat': 30, 'rol': 'Professor', 'cursos':'ASIX1A', 'moduls': 'M03, M07'},
    #     {'nom': 'Juanma', 'cognom': 'Bel', 'edat': 43, 'rol': 'Professor', 'cursos':'DAW2A, DAW2B', 'moduls': 'M05, M06'}
    # ]
    return render(request, 'teacher.html')