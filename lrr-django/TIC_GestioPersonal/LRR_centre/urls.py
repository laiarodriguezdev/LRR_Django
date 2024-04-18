from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('centre/student/', views.student, name='student'),
    path('centre/teacher/', views.teacher, name='teacher')
]