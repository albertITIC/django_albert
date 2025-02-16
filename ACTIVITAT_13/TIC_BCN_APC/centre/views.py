from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader # Importem el template


# Create your views here.
def index(request):
    texts = [{"text1": "Hola","text2":"mundo"}]
    template = loader.get_template('index.html')
    dades = template.render({'texts': texts})
        
    return HttpResponse(dades)

def alumne(request):
    alumnes = [
        {
            # Exemple 1
            "name":"Albert","surname1":"Penadés","surname2":"Casajús","email":"2023_albert.penades@iticbcn.cat","curse":"DAW2A","modules":"M6, M7, M8, ML" 
        },
        {
            # Exemple 2
            "name":"Víctor A.","surname1":"Fernández","surname2":"Álvarez","email":"2023_victor.fernandez@iticbcn.cat","curse":"DAW2A","modules":"M06, M07, M08, IA" 
        },
        {
            # Exemple 3
            "name":"Hugo","surname1":"Sansegundo","surname2":"Costantini","email":"2023_hugo.sansegundo@iticbcn.cat","curse":"DAW2A","modules":"M06, M07, M08, ML" 
        },
        {
            "name":"Adrián","surname1":"Navarro","surname2":"Pérez","email":"2023_adrian.navarro@iticbcn.cat","curse":"DAW2A","modules":"M06, M07, M08, Cloud"    
        },
        {
            "name":"Xavi","surname1":"Porras","surname2":"del Pino","email":"2023_xavier.porras@iticbcn.cat","curse":"DAW2A","modules":"M06, M07, M08"    
        },
        {
            "name":"Javier","surname1":"Giménez","surname2":"Sánchez","email":"2023_javier.gimenez@iticbcn.cat","curse":"DAW2A","modules":"M06, M07, M08, ML"    
        },
        {
            "name":"Milena","surname1":"Vardumyan","surname2":"Aleksanyan","email":"2023_milena.vardumyan@iticbcn.cat","curse":"DAW2A","modules":"M06, M07, M013, Big Data"    
        },
        {
            "name":"Daniel","surname1":"Vallespin","surname2":"Mellado","email":"2023_daniel.vallespin@iticbcn.cat","curse":"DAW2A","modules":"M06, M07, M08"    
        },
        {
            "name":"Félix Bequet","surname1":"Balbin","surname2":"Silva","email":"2023_felix.balbin@iticbcn.cat","curse":"DAW2A","modules":"M06, M07, M08, Big Data"    
        },
        {
            "name":"Lila","surname1":"Díez","surname2":"Zhou","email":"2023_lila.diez@iticbcn.cat","curse":"DAW2A","modules":"M06,M07,M08, ML"    
        },
        {
            "name":"Arman","surname1":"Mohammed","surname2":"Akther","email":"2023_arman.mohammed@iticbcn.cat","curse":"DAW2A","modules":"M06, M07, M08"    
        },
        {
            "name":"Natalia","surname1":"Casanellas","surname2":"Blanquer","email":"2023_natalia.casanellas@iticbcn.cat","curse":"DAW2A","modules":"M06, M07"    
        }, 
    ]
    
    template = loader.get_template('alumnes_centre.html')
    
    dades = template.render({'alumnes':alumnes})
    
    return HttpResponse(dades)

# Per professors
def professor(request):
    
    professors = [
        {
            "name":"Jordi", "surname1":"Quesada", "email":"jordi@gmail.com", "curse":"DAW2A", "modules":"M03"
        },
        {
            "name":"Juanma", "surname1":"Sànchez", "email":"juanma@gmail.com", "curse":"DAW2A", "modules":"M08"
        },
        {
            "name":"Roger", "surname1":"Sobrino", "email":"roger@gmail.com", "curse":"DAW2A", "modules":"M07"
        },
        {
            "name":"Oriol", "surname1":"Roca", "email":"oriol@gmail.com", "curse":"DAW2A", "modules":"M06"
        },
    ]  
    
    template = loader.get_template('professors_centre.html')    

    dades2 = template.render({'professors':professors})

    return HttpResponse(dades2)


# Apartat 2
def llistat_alumnes(request):
   llista_alumnes = [
        {"id": "1", "name": "Albert", "surname1": "Penadés", "surname2": "Casajús", "email": "2023_albert.penades@iticbcn.cat", "curse": "DAW2A", "modules": "M6, M7, M8, ML"},
        {"id": "2", "name": "Víctor A.", "surname1": "Fernández", "surname2": "Álvarez", "email": "2023_victor.fernandez@iticbcn.cat", "curse": "DAW2A", "modules": "M06, M07, M08, IA"},
        {"id": "3", "name": "Milena", "surname1": "Vardumyan", "surname2": "Aleksanyan", "email": "2023_milena.vardumyan@iticbcn.cat", "curse": "DAW2A", "modules": "M06, M07, M013, Big Data"},    
    ]
   
   template = loader.get_template('infoAlumnat.html')
    
   dades = template.render({"llista_alumnes": llista_alumnes})
    
   return HttpResponse(dades)

# def detall_alumne(request, id):
#     alumne_Obj = None
#     for i in 
    
#     template = loader.get_template('infoAlumnat.html') # Mirar-ho
    
#     dades = template.render({"llista_alumnes": llista_alumnes})
    
#     return HttpResponse(dades)
    
    
# def info_professor(request):
#     info_prof = [
#         {
#             "name":"1", "nom":"exemple", "email":"jordi@gmail.com", "curse":"DAW2A", "modules":"M03"
#         }
#     ]  
   
#     template = loader.get_template('infoAlumnat.html')    
#     info_alumnat = template.render({'info_alumnat': info_alumnat})
#     return HttpResponse(info_alumnat)