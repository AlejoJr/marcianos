from django.shortcuts import render, redirect
from apps.aeronave.forms import AeronaveForm
from apps.aeronave.models import Aeronave

# Create your views here.
def aeronave_lista(request):
    aeronave = Aeronave.objects.all().order_by('id')
    contexto = {'aeronaves': aeronave}
    return render(request, 'aeronave/listado_aeronave.html', contexto)

def aeronave_edit(request,id_aeronave):
    aeronave = Aeronave.objects.get(id=id_aeronave)
    if request.method == 'POST':
        form = AeronaveForm(request.POST, instance=aeronave)
        if form.is_valid():
            form.save()
        return redirect('aeronave:aeronave_lista')
    else:
        form = AeronaveForm(instance=aeronave)

    return render(request, 'aeronave/aeronave_form.html', {'form':form})

def aeronave_view(request):
    if request.method == 'POST':
        form = AeronaveForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('aeronave:aeronave_lista')
    else:
        form = AeronaveForm()

    return render(request, 'aeronave/aeronave_form.html', {'form':form})

