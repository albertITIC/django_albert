from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    # Modificar el path
    path('students/', views.alumne, name='alumnes'),    
    path('teachers/', views.professor, name='professors'),
    # Mostrar alumnes 
    path('alumnes/', views.llistat_alumnes, name='llistat_alumnes'),
    path('alumnes/<int:id>/', views.detall_alumne, name='detall_alumne')
]