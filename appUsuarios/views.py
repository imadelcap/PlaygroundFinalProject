from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from appUsuarios.forms import CustomUserCreationForm
from django.contrib.auth.views import LogoutView

from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
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
    
@staff_member_required  
def listar_usuarios(request):
    lista_usuarios = PerfilUsuario.objects.all()
    if request.POST:
        #print('###POST###')
        checked_items = request.POST.getlist("usuarios_checkbox")
        for a in lista_usuarios:
            a.usuario.is_staff = False
            a.usuario.save()
        for u in checked_items:
            #print('@' + u +'@')
            usuario_staff = PerfilUsuario.objects.get(usuario = u)
            #print(usuario_staff)
            #print(usuario_staff.usuario.is_staff)
            usuario_staff.usuario.is_staff = True
            usuario_staff.usuario.save()
        #lista_usuarios = PerfilUsuario.objects.all()    
        return render(request, 'index.html', {"mensaje":"Permisos correctamente"})
        #return render(request, 'usuarios/lista_usuarios.html', {'usuarios': lista_usuarios}) #Por alguna razon no me actualizaba bien, si iba a otra pagina, x ejemplo Ver perfil, y luego retornaba, si lograba ver correctamente la seleccion 

    else:
        return render(request, 'usuarios/lista_usuarios.html', {'usuarios': lista_usuarios})
