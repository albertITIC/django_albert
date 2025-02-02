from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # Modificar el path
    path('students/', views.alumne, name='alumnes'),    
    path('teachers/', views.professor, name='professors'),
    
]
