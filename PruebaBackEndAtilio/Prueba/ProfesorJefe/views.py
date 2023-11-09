from django.shortcuts import render
from ProfesorJefe.models import ProfJefe
from ProfesorJefe.forms import FormProfeJefe

def index(request):
    return render(request,r'C:\Users\choly\OneDrive\Escritorio\PruebaBackEndAtilio\Prueba\Templates\ProfesorJefe\index')

def MostrarDatos(request):
    ProfesoresJefes = ProfJefe.objects.all()
    data = {'profJefe' : ProfesoresJefes}
    return render(request,r'C:\Users\choly\OneDrive\Escritorio\PruebaBackEndAtilio\Prueba\Templates\ProfesorJefe\Ver',data)

def registrarProfJefe (request):
    form = FormProfeJefe()
    if request.method == 'POST' :
        form = FormProfeJefe(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data ={'form' : form}
    return render(request,r'C:\Users\choly\OneDrive\Escritorio\PruebaBackEndAtilio\Prueba\Templates\ProfesorJefe\registrar',data)

def eliminarProfesor(request,id):
    form = ProfJefe.objects.get(id = id)
    form.delete()
    return redirect('/ver')

def actualizarProfesor(request,id):
    profe = ProfJefe.objects.get(id = id)
    form = FormProfeJefe(instance=profe)
    if request.method == 'POST':
        form  = FormProfeJefe(request.POST, instance=profe)
        if form.is_valid():
            form.save()
        return index(request)
    data ={'form' : form}
    return render(request,r'C:\Users\choly\OneDrive\Escritorio\PruebaBackEndAtilio\Prueba\Templates\ProfesorJefe\registrar',data)

# Create your views here.
