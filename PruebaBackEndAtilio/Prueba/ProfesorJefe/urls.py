from django.contrib import admin
from django.urls import path

from ProfesorJefe import views

urlpatterns = [
    path('index/', views.index),
    path('MostrarDatos/',include('views.MostrarDatos')),
    path('registrarProfJefe/',views.registrarProfJefe)
    
]
