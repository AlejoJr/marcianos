from django.shortcuts import render, redirect
from apps.navenodriza.forms import NavenodrizaForm
from apps.navenodriza.models import NaveNodriza

# Create your views here.

def navenodriza_lista(request):
    navenodriza = NaveNodriza.objects.all().order_by('id')
    contexto = {'navesnodrizas':navenodriza}
    return render(request, 'navenodriza/listado_navesnodriza.html', contexto)

def navenodriza_edit(request,id_navenodriza):
    navenodriza = NaveNodriza.objects.get(id=id_navenodriza)
    if request.method == 'POST':
        form = NavenodrizaForm(request.POST, instance=navenodriza)
        if form.is_valid():
            form.save()
        return redirect('navenodriza:navenodriza_lista')
    else:
        form = NavenodrizaForm(instance=navenodriza)

    return render(request, 'navenodriza/navenodriza_form.html', {'form':form})

def navenodriza_delete(request,id_navenodriza):
    navenodriza = NaveNodriza.objects.get(id=id_navenodriza)
    if request.method == 'POST':
        navenodriza.delete()
        return redirect('navenodriza:navenodriza_lista')
    return render(request, 'navenodriza/navenodriza_delete.html', {'navenodriza':navenodriza})


def navenodriza_view(request):
    if request.method == 'POST':
        form = NavenodrizaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('navenodriza:navenodriza_lista')
    else:
        form = NavenodrizaForm()

    return render(request, 'navenodriza/navenodriza_form.html', {'form':form})

