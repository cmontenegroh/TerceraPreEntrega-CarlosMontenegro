from django.shortcuts import render

# Create your views here.
from .models import Aula, Tutor, Estudiante, Desafio
from django.http import HttpResponse
from .forms import AulaForm, TutorForm, EstudianteForm, DesafioForm


def crear_aula(request):
    nombre_aula="Programacion Basica"
    comision_aula=99888
    print("creando aula")
    aula=Aula(nombre=nombre_aula, comision=comision_aula)
    aula.save()
    respuesta=f"Aula creada: {aula.nombre} - {aula.comision}"
    return HttpResponse(respuesta)

def listar_aulas(request):
    aulas=Aula.objects.all()
    respuesta=""
    for aula in aulas:
        respuesta+=f"{aula.nombre} - {aula.comision}<br>"
    return HttpResponse(respuesta)


#AQUI TENGO QUE COMPLETAR CON LA FUNCION DE LISTAR CURSOS DE LA CLASE 18

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def tutores(request):
    if request.method=="POST":
        form=TutorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            profesion=info["profesion"]
            tutor=Tutor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            tutor.save()
            formulario_tutor=TutorForm()
            return render(request,"AppCoder/tutores.html", {"mensaje":"Registrado con exito", "formulario":formulario_tutor})
        else:
            return render(request,"AppCoder/tutores.html", {"mensaje":"Registro no valido"})
    else:
        formulario_tutor=TutorForm()
            
       
    return render(request,"AppCoder/tutores.html", {"formulario":formulario_tutor})


def estudiantes(request):
    if request.method=="POST":
        form=EstudianteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            estudiante=Estudiante(nombre=nombre, apellido=apellido, email=email)
            estudiante.save()
            formulario_estudiante=EstudianteForm()
            return render(request,"AppCoder/estudiantes.html", {"mensaje":"Registrado con exito", "formulario":formulario_estudiante})
        else:
            return render(request,"AppCoder/estudiantes.html", {"mensaje":"Registro no valido"})
    else:
        formulario_estudiante=EstudianteForm()
    
    
    return render(request,"AppCoder/estudiantes.html", {"formulario":formulario_estudiante})




def desafios(request):
    if request.method=="POST":
        form=DesafioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            fecha_entrega=info["fecha_entrega"]
            entregado=info["entregado"]
            desafio=Desafio(nombre=nombre, fecha_entrega= fecha_entrega, entregado=entregado)
            desafio.save()
            formulario_desafios=DesafioForm()
            return render(request,"AppCoder/desafios.html", {"mensaje":"Registrado con exito", "formulario":formulario_desafios})
        else:
            return render(request,"AppCoder/desafios.html")
    else:
        formulario_desafios=DesafioForm()
        return render(request,"AppCoder/desafios.html", {"formulario":formulario_desafios})

def aulas(request):
    if request.method=="POST":
        form=AulaForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            comision=info["comision"]
            aula=Aula(nombre=nombre, comision=comision)
            aula.save()
            return render(request,"AppCoder/aulas.html", {"mensaje":"Aula Creada"})
    else:
        formulario_aula=AulaForm()
        return render(request, "AppCoder/aulas.html", {"formulario":formulario_aula})
    
    
def busquedaComision(request):
    return render(request,"AppCoder/busquedaComision.html")

def buscar(request):
    comision=request.GET["comision"]
    if comision!="":
        aulas=Aula.objects.filter(comision__icontains=comision)
        return render(request,"AppCoder/resultadosBusqueda.html", {"aulas":aulas})
    else:
        return render(request,"AppCoder/busquedaComision.html",  {"mensaje":"Ingrese nuevamente los datos"})

        
    
    
    
    
    