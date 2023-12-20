from django.shortcuts import render, redirect

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

def listar_accesorios(request):
    lista_acc = Accesorio.objects.all()
    return render(request, 'stock/lista_accesorios.html', {'accesorios': lista_acc})

def listar_bicicletas(request):
    lista_bicis = ModeloBicicleta.objects.all()
    return render(request, 'stock/lista_bicicletas.html', {'bicicletas': lista_bicis})

def eliminar_bicicleta(request, marca_bicicleta, tipo_bicicleta, rodado_bicicleta):
    bicicleta = ModeloBicicleta.objects.get(marca = marca_bicicleta, tipo = tipo_bicicleta, rodado = rodado_bicicleta)
    bicicleta.delete()
    return redirect('listar modelos de bicicletas')

def eliminar_accesorio(request, marca_accesorio, tipo_accesorio):
    accesorio = Accesorio.objects.get( marca = marca_accesorio, tipo = tipo_accesorio)
    accesorio.delete()
    return redirect('listar accesorios')

def editar_accesorio(request, marca_accesorio, tipo_accesorio):
    accesorio = Accesorio.objects.filter( marca = marca_accesorio, tipo = tipo_accesorio)

    formulario = AccesorioFormulario(request.POST)
    
    print('@@@@@@@@@@') #Debug
    print(marca_accesorio, tipo_accesorio) #Debug

    if formulario.is_valid():
        datos = formulario.cleaned_data
        accesorio.tipo = datos["tipo"]
        accesorio.marca = datos["marca"]
        accesorio.descripcion = datos["descripcion"]
        accesorio.stock = datos ['stock']
        accesorio.save()
        return render(request, 'index.html', {"mensaje":"Accesorio " + accesorio.tipo + " modificado correctamente"})
    else:
        accesorio = Accesorio.objects.get( marca = marca_accesorio, tipo = tipo_accesorio)
        datos_iniciales = {'tipo': accesorio.tipo, 'marca': accesorio.marca, 'descripcion': accesorio.descripcion, 'stock': accesorio.stock}      
        formulario = AccesorioFormulario(initial=datos_iniciales)
        return render(request, 'stock/editar_accesorio.html', {'formulario': formulario })

def buscar_accesorio(request):

    formulario = AccesorioFormulario()
    return render(request, 'stock/buscar_accesorio.html', {'formulario': formulario })

def buscar_modelo_bicicleta(request):

    formulario = ModeloBicicletaFormulario()
    return render(request, 'stock/buscar_modelo_bicicleta.html', {'formulario': formulario })

