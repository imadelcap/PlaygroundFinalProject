from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()

class ModeloBicicletaFormulario(forms.Form):
    marca = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=30)
    rodado = forms.IntegerField()

class AccesorioFormulario(forms.Form):
    tipo = forms.CharField() 
    marca = forms.CharField()
    descripcion = forms.CharField()