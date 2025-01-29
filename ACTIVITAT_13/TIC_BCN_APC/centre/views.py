from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader # Importem el template


# Create your views here.

def alumne(request):
    alumnes = [
        {
            # Exemple 1
            "name":"Albert","surname1":"Penadés","surname2":"Casajús","email":"albert@gmail.com","curse":"DAW2A","modules":"M6, M7, M8, ML" 
        },
        {
            # Exemple 2
            "name":"Víctor","surname1":"Fernández","surname2":"Álvarez","email":"victor@gmail.com","curse":"DAW2A","modules":"M6, M7, M8, IA" 
        },
        {
            # Exemple 3
            "name":"ejemplo","surname1":"ejemplo","surname2":"ejemplo","email":"ejemplo@gmail.com","curse":"DAW2A","modules":"ejemplo" 
        },
        
    ]
    
    template = loader.get_template('alumnes_centre.html')
    
    dades = template.render({'alumnes':alumnes})
    
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
        'moduls':professor["modules"],
        
        })
    
    return HttpResponse(dades)

# Versió resumida
# def index(request):
#     alumne = {{"name":"Albert", "surname":"Penades", "age":21}}
#     return render(request, 'index_centre.html', {"name":alumne["name"], "surname":alumne["surname"], "age":alumne["age"]})

# def students(request):
#     template = loader.get_template('index_centre.html')
#     return HttpResponse(template.render())