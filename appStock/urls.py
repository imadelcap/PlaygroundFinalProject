from django.urls import path

from appStock.views import formulario_accesorio, formulario_modelo_bicicleta, buscar_accesorio, buscar_modelo_bicicleta

urlpatterns = [
    path('crear_accesorio/', formulario_accesorio, name='crear accesorio'),
    path('crear_modelo_de_bicicleta/', formulario_modelo_bicicleta, name='crear modelo de bicicleta'),
    path('buscar_accesorio/', buscar_accesorio, name='buscar accesorio'),
    path('buscar_modelo_de_bicicleta/', buscar_modelo_bicicleta, name='buscar modelo de bicicleta')
]