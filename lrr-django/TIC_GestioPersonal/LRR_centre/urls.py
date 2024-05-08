from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('centre/student/', views.student, name='student'),
    path('centre/teacher/', views.teacher, name='teacher'),
    path('user-form/', views.user_form, name='user_form'),
    path('update-user/<str:pk>/', views.update_user, name='update-user'),
    path('delete-user/<str:pk>/', views.delete_user, name='delete-user')
]