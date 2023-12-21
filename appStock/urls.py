from django.urls import path

from appStock.views import formulario_accesorio, formulario_modelo_bicicleta, buscar_accesorio, buscar_modelo_bicicleta, listar_accesorios, listar_bicicletas, eliminar_accesorio, eliminar_bicicleta, editar_accesorio, editar_bicicleta

urlpatterns = [
    path('crear_accesorio/', formulario_accesorio, name='crear accesorio'),
    path('crear_modelo_de_bicicleta/', formulario_modelo_bicicleta, name='crear modelo de bicicleta'),
    path('listar_accesorios/', listar_accesorios, name='listar accesorios'),
    path('listar_modelos_de_bicicletas/', listar_bicicletas, name='listar modelos de bicicletas'),
    path('eliminar_accesorio/<str:marca_accesorio>/<str:tipo_accesorio>', eliminar_accesorio, name='eliminar_accesorio'),
    path('eliminar_bicicleta/<str:marca_bicicleta>/<str:tipo_bicicleta>/<int:rodado_bicicleta>', eliminar_bicicleta, name='eliminar_bicicleta'),
    path('editar_accesorio/<str:marca_accesorio>/<str:tipo_accesorio>', editar_accesorio, name='editar_accesorio'),
    path('editar_bicicleta/<str:marca_bicicleta>/<str:tipo_bicicleta>/<int:rodado_bicicleta>', editar_bicicleta, name='editar_bicicleta'),
    path('buscar_accesorio/', buscar_accesorio, name='buscar accesorio'),
    path('buscar_modelo_de_bicicleta/', buscar_modelo_bicicleta, name='buscar modelo de bicicleta')
]