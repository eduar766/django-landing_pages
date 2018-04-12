from django.shortcuts import render, redirect
from .forms import EnviarMensajeForm, EnviarMensajeForm
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    form = EnviarMensajeForm()
    context = {'form': form }
    return render(request, 'easyway/index.html', context)

def gracias(request):
    return render(request, 'easyway/gracias.html')

def contenido(request):
    form = EnviarMensajeForm()
    context = {'form': form }
    return render(request, 'easyway/contenidos.html', context)

@require_POST
def comentar(request):
    comentarform = EnviarMensajeForm(request.POST)

    if comentarform.is_valid():
        nuevo_comentario = comentarform.save()

    return redirect('gracias')
