from django.urls import path

from appUsuarios.views import registro_usuario, login_usuario, Logout

urlpatterns = [
    path('login/', login_usuario, name='login'),
    path('registro/', registro_usuario, name='registro'),
    path('logout/', Logout.as_view(), name='logout'),
]
