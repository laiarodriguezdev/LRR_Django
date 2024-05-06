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
    # alumnes = [
    #     {'nom': 'Laia', 'cognom': 'Rodríguez',  'rol': 'Estudiant', 'link':'+INFO'},
    #     {'nom': 'Harpreet', 'cognom': 'Kaur', 'rol': 'Estudiant',  'link':'+INFO'}
    # ]
    return render(request, 'student.html')

def teacher(request):
    # teachers = [
    #     {'nom': 'Oscar', 'cognom': 'Rovira', 'edat': 30, 'rol': 'Professor', 'cursos':'ASIX1A', 'moduls': 'M03, M07'},
    #     {'nom': 'Juanma', 'cognom': 'Bel', 'edat': 43, 'rol': 'Professor', 'cursos':'DAW2A, DAW2B', 'moduls': 'M05, M06'}
    # ]
    return render(request, 'teacher.html')