from django.shortcuts import render, redirect
from apps.pasajero.forms import PasajeroForm
from apps.pasajero.models import Pasajero

# Create your views here.
def pasajero_lista(request):
    pasajero = Pasajero.objects.all().order_by('id')
    contexto = {'pasajeros':pasajero}
    return render(request, 'pasajero/listado_pasajeros.html', contexto)

def pasajero_edit(request,id_pasajero):
    pasajero = Pasajero.objects.get(id=id_pasajero)
    if request.method == 'POST':
        form = PasajeroForm(request.POST, instance=pasajero)
        if form.is_valid():
            form.save()
        return redirect('pasajero:pasajero_lista')
    else:
        form = PasajeroForm(instance=pasajero)

    return render(request, 'pasajero/pasajero_form.html', {'form':form})

def pasajero_delete(request,id_pasajero):
    pasajero = Pasajero.objects.get(id=id_pasajero)
    if request.method == 'POST':
        pasajero.delete()
        return redirect('pasajero:pasajero_lista')
    return render(request, 'pasajero/pasajero_delete.html', {'pasajero':pasajero})

def pasajero_view(request):
    if request.method == 'POST':
        form = PasajeroForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('pasajero:pasajero_lista')
    else:
        form = PasajeroForm()

    return render(request, 'pasajero/pasajero_form.html', {'form':form})

