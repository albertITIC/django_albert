from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader # Importem el template


# Create your views here.
def index(request):
     alumne = {"name":"Albert", "surname":"Penadés", "age":21}
     template = loader.get_template('index_centre.html')
     dades = template.render({'nom':alumne["name"],'cognom':alumne["surname"],'edat':alumne["age"]})
     return HttpResponse(dades)


# Versió resumida
# def index(request):
#     alumne = {{"name":"Albert", "surname":"Penades", "age":21}}
#     return render(request, 'index_centre.html', {"name":alumne["name"], "surname":alumne["surname"], "age":alumne["age"]})