from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader # Importem el template


# Create your views here.

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


def info_alumnat(request):
      
    info_alumnat = [
        {
            "name":"1", "nom":"exemple", "email":"jordi@gmail.com", "curse":"DAW2A", "modules":"M03"
        }
    ]  
    
    template = loader.get_template('llibres.html')    

    info_alumnat = template.render({'info_alumnat': info_alumnat})

    return HttpResponse(info_alumnat)


def info_professor(request):
    info_prof = [
        {
            "name":"1", "nom":"exemple", "email":"jordi@gmail.com", "curse":"DAW2A", "modules":"M03"
        }
    ]  
    
    template = loader.get_template('infoAlumnat.html')    

    info_alumnat = template.render({'info_alumnat': info_alumnat})

    return HttpResponse(info_alumnat)