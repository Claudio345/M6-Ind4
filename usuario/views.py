from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required
def index(request):
    usuarios = Usuario.objects.all()
    print(usuarios)
    return render(
        request,
        'index.html',
        { 'usuarios': usuarios }
    )

@login_required
@permission_required('usuarios.add_usuario', raise_exception=True)
def formulario(request):
    print('Hola soy el Formulario - def formulario')
    if request.method == 'POST':
        form = UsuarioForm(request.POST) # Aqui en el request.POST viene nombre, stock, categoria, imagen
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/usuario')
    else:
        form = UsuarioForm()
    return render(
        request,
        'usuario_form.html',
        {'form': form }
    )
@login_required
def detail(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'detail.html', context={'usuario': usuario})

@login_required
@permission_required('usuarios.delete_usuario', raise_exception=False)
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario:index')
    return redirect('usuario:index')

@login_required
@permission_required('usuarios.change_usuario', raise_exception=False)
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario:index')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario_form.html', {'form': form, 'is_editing': True})