from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader # Importem el template


# Create your views here.

def alumne(request):
    alumne = {
        "name":"Albert",
        "surname1":"Penadés",
        "surname2":"Casajús", 
        "email":"albert@gmail.com", 
        "curse":"DAW2A", 
        "modules":"M6, M7, M8, M9" 
    }
    
    template = loader.get_template('index_centre.html')
    
    dades = template.render({
        'nom':alumne["name"],
        'cognom1':alumne["surname1"],
        'cognom2':alumne["surname2"],
        'correu':alumne["email"],
        'curs':alumne["curse"],
        'moduls':alumne["modules"]  
    })
    
    return HttpResponse(dades)

# Per professors
def professor(request):
    professor = {
        "name":"Roger",
        "surname1":"Sobrino",
        "surname2":"Gil", 
        "email":"roger@gmail.com", 
        "curse":"DAW2A", 
        "modules":"M6, M13" 
    }
   
    template = loader.get_template('professors_centre.html')
    
    dades = template.render({
        'nom':professor["name"],
        'cognom1':professor["surname1"],
        'cognom2':professor["surname2"],
        'correu':professor["email"],
        'curs':professor["curse"],
        'moduls':professor["modules"]
        })
    
    return HttpResponse(dades)

# Versió resumida
# def index(request):
#     alumne = {{"name":"Albert", "surname":"Penades", "age":21}}
#     return render(request, 'index_centre.html', {"name":alumne["name"], "surname":alumne["surname"], "age":alumne["age"]})