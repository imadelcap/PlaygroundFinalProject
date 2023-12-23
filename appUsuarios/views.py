from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from appUsuarios.forms import CustomUserCreationForm
from django.contrib.auth.views import LogoutView

from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from appUsuarios.models import PerfilUsuario

def login_usuario(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            
            login(request, user)
            if user.is_staff:
                print('@@@@@@@@@@@@ Staff')
            return render(request, "index.html", {"mensaje": f'Bienvenid@ {user.username}'})
        else:
            return render(request, 'usuarios/login.html', {"formulario": formulario})
    
    else:
        formulario = AuthenticationForm()
        return render(request, "usuarios/login.html", {"formulario": formulario})
    
def registro_usuario(request):

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            formulario.save()
            return render(request,"index.html" ,  {"mensaje":"Usuario " + username + " registrado correctamente"})
        else:
            return render(request, 'usuarios/registro.html', {"formulario": formulario})

    else:
        formulario = CustomUserCreationForm()
        return render(request,"usuarios/registro.html" ,  {"formulario": formulario})

class Logout(LogoutView):
    template_name = "usuarios/logout.html"

class PerfilUsuarioCreateView(LoginRequiredMixin, CreateView):
    model = PerfilUsuario
    template_name = 'usuarios/crear_perfil.html'
    success_url = reverse_lazy('ver perfil')
    fields = ['usuario', 'imagen', 'rol']
    login_url = 'usuarios/login'

class PerfilUsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = PerfilUsuario
    template_name = 'usuarios/editar_perfil.html'
    success_url = reverse_lazy('ver perfil')
    fields = ['imagen', 'rol']
    login_url = 'usuarios/login'

@login_required(login_url = 'login')
def perfil_usuario(request):
    try:
        request.user.perfil
        return render(request, 'usuarios/perfil.html')
    except:
        return redirect('crear perfil')