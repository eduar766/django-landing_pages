from django.shortcuts import render, redirect
from .forms import MensajeBailanteForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    form = MensajeBailanteForm()
    context = {'form': form}
    return render(request, 'bailante/index.html', context)

def carousel(request):
    return render(request, 'bailante/carousel.html')

@require_POST
def sendForm(request):
    form = MensajeBailanteForm(request.POST)

    if form.is_valid():
        nuevo_form = form.save()

    return redirect('index')
