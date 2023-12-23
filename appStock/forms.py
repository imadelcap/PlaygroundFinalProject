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