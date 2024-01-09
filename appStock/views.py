from django.shortcuts import render, redirect

from appStock.models import ModeloBicicleta, Accesorio
from appStock.forms import AccesorioFormulario, ModeloBicicletaFormulario

from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required

from datetime import datetime

#@staff_member_required
def formulario_modelo_bicicleta(request):
    #No permito hacer altas de inventario a personas que no tienen dicho privilegio
    if not request.user.is_staff:
        return render(request, 'index.html',  {"mensaje":"No tiene permisos para ejecutar esta acción."})    
    else:
        if request.method == 'POST':
            modelo_bicicleta = ModeloBicicleta(
                marca = request.POST['marca'], 
                tipo = request.POST['tipo'], 
                rodado = request.POST['rodado'],
                stock = request.POST['stock'],
                creado = datetime.now(),
                )
            modelo_bicicleta.save()
            return render(request, 'index.html',  {"mensaje":"Bicicleta " + modelo_bicicleta.marca + " ingresada correctamente"})    
        
        return render(request, 'stock/formulario_modelo_bicicleta.html')

def formulario_accesorio(request):
    
    if not request.user.is_staff:
        return render(request, 'index.html',  {"mensaje":"No tiene permisos para ejecutar esta acción."})    
    else:
        if request.method == 'POST':
            formulario = AccesorioFormulario(request.POST)
        
            if formulario.is_valid():
                datos = formulario.cleaned_data
                accesorio = Accesorio(
                    tipo = datos["tipo"], 
                    marca = datos["marca"], 
                    descripcion = datos["descripcion"],
                    stock = datos ["stock"],
                    creado = datetime.now(),
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

@staff_member_required    #No permito hacer modificaciones de inventario a personas que no tienen dicho privilegio
def eliminar_bicicleta(request, marca_bicicleta, tipo_bicicleta, rodado_bicicleta):
    bicicleta = ModeloBicicleta.objects.get(marca = marca_bicicleta, tipo = tipo_bicicleta, rodado = rodado_bicicleta)
    bicicleta.delete()
    return redirect('listar modelos de bicicletas')

@staff_member_required ()    #No permito hacer modificaciones de inventario a personas que no tienen dicho privilegio
def eliminar_accesorio(request, marca_accesorio, tipo_accesorio):
    accesorio = Accesorio.objects.get( marca = marca_accesorio, tipo = tipo_accesorio)
    accesorio.delete()
    return redirect('listar accesorios')

@staff_member_required
def editar_bicicleta(request, marca_bicicleta, tipo_bicicleta, rodado_bicicleta):
    bicicleta = ModeloBicicleta.objects.get(marca = marca_bicicleta, tipo = tipo_bicicleta, rodado = rodado_bicicleta)
    formulario = ModeloBicicletaFormulario(request.POST)
    
    if formulario.is_valid():
        
        datos = formulario.cleaned_data
        bicicleta.marca = datos['marca'] 
        bicicleta.tipo = datos['tipo']
        bicicleta.rodado = datos['rodado']
        bicicleta.stock = datos['stock']
        bicicleta.modificado = datetime.now()
        bicicleta.save()

        return render(request, 'index.html',  {"mensaje":"Bicicleta " + bicicleta.marca + " modificada correctamente"})    
    else:
        datos_iniciales = {'marca':bicicleta.marca, 'tipo':bicicleta.tipo, 'rodado':bicicleta.rodado, 'stock':bicicleta.stock}
        formulario = ModeloBicicletaFormulario(initial=datos_iniciales)
    return render(request, 'stock/editar_bicicleta.html', {'formulario':formulario})

@staff_member_required
def editar_accesorio(request, marca_accesorio, tipo_accesorio):
    accesorio = Accesorio.objects.get( marca = marca_accesorio, tipo = tipo_accesorio)
    formulario = AccesorioFormulario(request.POST)
    
    #print('@@@@@@@@@@', marca_accesorio, tipo_accesorio) #Debug problema pasaje parametros html
    
    if formulario.is_valid():
        datos = formulario.cleaned_data
        accesorio.tipo = datos["tipo"]
        accesorio.marca = datos["marca"]
        accesorio.descripcion = datos["descripcion"]
        accesorio.stock = datos ['stock']
        accesorio.modificado = datetime.now()
        accesorio.save()
        return render(request, 'index.html', {"mensaje":"Accesorio " + accesorio.tipo + " modificado correctamente"})
    else:
        datos_iniciales = {'tipo': accesorio.tipo, 'marca': accesorio.marca, 'descripcion': accesorio.descripcion, 'stock': accesorio.stock}      
        formulario = AccesorioFormulario(initial=datos_iniciales)
        return render(request, 'stock/editar_accesorio.html', {'formulario': formulario })

def buscar_accesorio(request):
    if request.GET.get('caracteristica',False):
        b_criterio = request.GET['criterio']
        b_caracteristica = request.GET['caracteristica']
        #print('##############'+b_criterio+b_caracteristica)
        if b_criterio == 'tipo':
            accesorios = Accesorio.objects.filter(tipo__contains = b_caracteristica)
            return render(request, 'stock/lista_accesorios.html', {'accesorios': accesorios})
        elif b_criterio == 'marca':
            accesorios = Accesorio.objects.filter(marca__contains = b_caracteristica)
            return render(request, 'stock/lista_accesorios.html', {'accesorios': accesorios})
        elif b_criterio == 'descripcion':
            accesorios = Accesorio.objects.filter(descripcion__contains = b_caracteristica)
            return render(request, 'stock/lista_accesorios.html', {'accesorios': accesorios})
    else:
        return render(request, 'stock/buscar_accesorio.html')

def buscar_modelo_bicicleta(request):
    if request.GET.get('caracteristica',False):
        b_criterio = request.GET['criterio']
        b_caracteristica = request.GET['caracteristica']
        if b_criterio == 'marca':
            bicicletas = ModeloBicicleta.objects.filter(marca__contains = b_caracteristica)
            return render(request, 'stock/lista_bicicletas.html', {'bicicletas': bicicletas})
        elif b_criterio == 'tipo':
            bicicletas = ModeloBicicleta.objects.filter(tipo__contains = b_caracteristica)
            return render(request, 'stock/lista_bicicletas.html', {'bicicletas': bicicletas})
        elif b_criterio == 'rodado':
            bicicletas = ModeloBicicleta.objects.filter(rodado = int(b_caracteristica))
            return render(request, 'stock/lista_bicicletas.html', {'bicicletas': bicicletas})
    else:
        return render(request, 'stock/buscar_modelo_bicicleta.html')

