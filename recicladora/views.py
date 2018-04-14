from django.shortcuts import render, redirect
from .forms import RecicladoraMensajeForms, GaleriaForms
from .models import RecicladoraMensaje, Galeria
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):

    return render(request, 'recicladora/index.html')

def servicios(request):
    return render(request, 'recicladora/servicios.html')

def como_reciclar(request):
    return render(request, 'recicladora/como-reciclar.html')

def galeria(request):
    return render(request, 'recicladora/galeria.html')

def nosotros(request):
    return render(request, 'recicladora/nosotros.html')

def cargaFoto(request):
    form = GaleriaForms()
    context = {'form': form}
    return render(request, 'recicladora/carga.html', context)

def contacto(request):
    form = RecicladoraMensajeForms()
    context = {'form': form}
    return render(request, 'recicladora/contacto.html', context)

@require_POST
def sendForm(request):
    form = RecicladoraMensajeForms(request.POST)

    if form.is_valid():
        new_form = form.save()

    return redirect('index')

@require_POST
def sendFormImg(request):
    form = GaleriaForms(request.POST)

    if form.is_valid():
        new_form = form.save()

    return redirect('carga')


def upload(request):
    form = GaleriaForms(request.POST)
    if form.image.data:
        image_data = request.FILES[form.image.name].read()
        open(os.path.join(pic_folder, form.image.data), 'w').write(image_data)
