from django import forms

class ModeloBicicletaFormulario(forms.Form):
    marca = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=30)
    rodado = forms.IntegerField()
    stock = forms.IntegerField()

class AccesorioFormulario(forms.Form):
    tipo = forms.CharField() 
    marca = forms.CharField()
    descripcion = forms.CharField()
    stock = forms.IntegerField()

# Genero otras clases de formularios, con todos los campos opcionales, para implementar la búsqueda como lo deseo

class BusquedaModeloBicicletaFormulario(forms.Form):
    opciones = ((1,'marca'),(2,'tipo'),(3,'rodado'))
    criterio = forms.ChoiceField(choices= opciones)
    caracteristica = forms.CharField(max_length=20)

class BusquedaAccesorioFormulario(forms.Form):
    opciones = ((1,'marca'),(2,'tipo'))
    criterio = forms.ChoiceField(choices= opciones)
    caracteristica = forms.CharField(max_length=20)