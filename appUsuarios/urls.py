from django.urls import path

from appUsuarios.views import registro_usuario, login_usuario, Logout, PerfilUsuarioCreateView, PerfilUsuarioUpdateView, perfil_usuario

urlpatterns = [
    path('login/', login_usuario, name='login'),
    path('registro/', registro_usuario, name='registro'),
    path('logout/', Logout.as_view(), name='logout'),
    path('perfil/', perfil_usuario, name = 'ver perfil'),
    path('crear_perfil/', PerfilUsuarioCreateView.as_view(), name = 'crear perfil'),
    path('<pk>/editar_perfil/', PerfilUsuarioUpdateView.as_view(), name = 'editar perfil')
]
