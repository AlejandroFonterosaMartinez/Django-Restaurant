from django.shortcuts import render, redirect,get_object_or_404
from .models import Plato
from .forms import NuevoPlatoForm


def carta_restaurante(request):
    platos = Plato.objects.all()
    return render(request, 'carta_restaurante.html', {'platos': platos})


def cargar_plato(request):
    if request.method == 'POST':
        form = NuevoPlatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('carta_restaurante')
    else:
        form = NuevoPlatoForm()
    return render(request, 'cargar_plato.html', {'form': form})


def visualizar_platos(request):
    platos = Plato.objects.all()
    return render(request, 'visualizar_platos.html', {'platos': platos})



