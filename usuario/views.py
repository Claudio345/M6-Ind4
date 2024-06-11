from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def index(request):
    usuarios = Usuario.objects.all()
    print(usuarios)
    return render(
        request,
        'index.html',
        { 'usuarios': usuarios }
    )
    
def formulario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST) # Aqui en el request.POST viene nombre, stock, categoria, imagen
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/usuarios')
    else:
        form = UsuarioForm()
    return render(
        request,
        'usuario_form.html',
        {'form': form }
    )

def detail(request, usuario_id):
    usuario = get_object_or_404(usuario, id=usuario_id)
    return render(request, 'detail.html', context={'usuario': usuario})