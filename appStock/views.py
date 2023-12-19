from django.shortcuts import render

from django.shortcuts import render
from appStock.models import ModeloBicicleta, Accesorio
from appStock.forms import AccesorioFormulario, ModeloBicicletaFormulario

#@login_required(login_url="login")

def formulario_modelo_bicicleta(request):
    if request.method == 'POST':
        modelo_bicicleta = ModeloBicicleta(
            marca = request.POST['marca'], 
            tipo = request.POST['tipo'], 
            rodado = request.POST['rodado'],
            stock = request.POST['stock']
            )
        modelo_bicicleta.save()

        return render(request, 'index.html',  {"mensaje":"Bicicleta " + modelo_bicicleta.marca + " ingresada correctamente"})    
    
    return render(request, 'stock/formulario_modelo_bicicleta.html')


def formulario_accesorio(request):
    if request.method == 'POST':
        formulario = AccesorioFormulario(request.POST)
     
        if formulario.is_valid():
            datos = formulario.cleaned_data
            accesorio = Accesorio(
                tipo = datos["tipo"], 
                marca = datos["marca"], 
                descripcion = datos["descripcion"],
                stock = datos ['stock']
                )
            accesorio.save()
            return render(request, 'index.html', {"mensaje":"Accesorio " + accesorio.tipo + " ingresado correctamente"})
           
    formulario = AccesorioFormulario()
    return render(request, 'stock/formulario_accesorio.html', {'formulario': formulario })

def buscar_accesorio(request):
    return render(request, 'stock/formulario_buscar_accesorio.html')

def buscar_modelo_bicicleta(request):
    return render(request, 'stock/formulario_buscar_modelo_bicicleta.html')

