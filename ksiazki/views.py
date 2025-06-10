from django.shortcuts import render, redirect, get_object_or_404
from .models import Ksiazka
from .forms import KsiazkaForm

def lista_ksiazek(request):
    ksiazki = Ksiazka.objects.all()
    return render(request, 'ksiazki/lista.html', {'ksiazki': ksiazki})

def dodaj_ksiazke(request):
    if request.method == 'POST':
        form = KsiazkaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ksiazek')
    else:
        form = KsiazkaForm()
    return render(request, 'ksiazki/formularz.html', {'form': form})

def edytuj_ksiazke(request, pk):
    ksiazka = get_object_or_404(Ksiazka, pk=pk)
    if request.method == 'POST':
        form = KsiazkaForm(request.POST, instance=ksiazka)
        if form.is_valid():
            form.save()
            return redirect('lista_ksiazek')
    else:
        form = KsiazkaForm(instance=ksiazka)
    return render(request, 'ksiazki/formularz.html', {'form': form})


def usun_ksiazke(request, pk):
    ksiazka = get_object_or_404(Ksiazka, pk=pk)
    if request.method == 'POST':
        ksiazka.delete()
        return redirect('lista_ksiazek')
    return render(request, 'ksiazki/usuniecie.html', {'ksiazka': ksiazka})
