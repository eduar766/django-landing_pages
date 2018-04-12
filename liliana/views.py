from django.shortcuts import render, redirect
from .forms import MensajeLilianaForm
from .models import MensajeLiliana
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    form = MensajeLilianaForm()
    context = {'form': form}
    return render(request, 'liliana/index.html', context)

def gracias(request):
    return render(request, 'liliana/thank-you.html')

@require_POST
def sendEmail(request):
    form = MensajeLilianaForm(request.POST)
    if form.is_valid():
        new_form = form.save()

    return redirect('gracias')
