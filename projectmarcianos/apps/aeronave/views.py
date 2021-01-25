from django.shortcuts import render, redirect
from apps.aeronave.forms import AeronaveForm, GestionarPasajeroForm, ListadoRevisionNaveForm
from apps.aeronave.models import Aeronave, GestionPasajeros, ListadoRevisionNave, HistorialNaveRevisada, RegistroNaveRevisada
from apps.pasajero.models import Pasajero
import datetime

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

def aeronave_delete(request,id_aeronave):
    aeronave = Aeronave.objects.get(id=id_aeronave)
    if request.method == 'POST':
        aeronave.delete()
        return redirect('aeronave:aeronave_lista')
    return render(request, 'aeronave/aeronave_delete.html', {'aeronave':aeronave})

def aeronave_view(request):
    if request.method == 'POST':
        form = AeronaveForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('aeronave:aeronave_lista')
    else:
        form = AeronaveForm()

    return render(request, 'aeronave/aeronave_form.html', {'form':form})

def gestionar_pasajero(request):
    if request.method == 'POST':
        accion = ''
        estado = True
        valueActivo = True
        valueId = 0
        postEstado = request.POST['activo']
        form = GestionarPasajeroForm(request.POST)
        pasajeroExist = GestionPasajeros.objects.filter(pasajero=request.POST['pasajero'], activo=True).exists()
        if(pasajeroExist and postEstado == 'True'):
            objetouno = GestionPasajeros.objects.filter(pasajero=request.POST['pasajero'], activo=True).values()
            valueAeronave = objetouno[0]['aeronave_id']
            nameAeronave = Aeronave.objects.filter(id=valueAeronave).values('nombre')
            form.add_error('pasajero','El Pasajero ya se encuentra en la Aeronave '+ nameAeronave[0]['nombre'])
        else:
            objetoExist = GestionPasajeros.objects.filter(pasajero=request.POST['pasajero'], aeronave=request.POST['aeronave']).exists()

            if (objetoExist):
                objeto = GestionPasajeros.objects.filter(pasajero=request.POST['pasajero'],
                                                         aeronave=request.POST['aeronave']).values()
                valueId = objeto[0]['id']
                valueActivo = objeto[0]['activo']
                valueAeronave = objeto[0]['aeronave_id']
                if (valueActivo == True and postEstado == 'True'):
                    nameAeronave = Aeronave.objects.filter(id=valueAeronave).values('nombre')
                    form.add_error('pasajero',
                                   'El Pasajero ya se encuentra asignado a la Aeronave: ' + nameAeronave[0]['nombre'])
                else:
                    accion = 'actualizar'
                    if (postEstado == 'True'):
                        valueActivo = True
                    else:
                        valueActivo = False
            else:
                if(objetoExist == False and postEstado == 'False'):
                    form.add_error('pasajero','No puede bajar a este pasajero ya que no se encuentra en la Aeronave asignado')
                else:
                    number_pasajeros_aeronave = GestionPasajeros.objects.filter(activo=True,
                                                                                aeronave=request.POST[
                                                                                    'aeronave']).count()
                    maxPasajeros = Aeronave.objects.filter(id=request.POST['aeronave']).values('max_marcianos')
                    cupoMaximo = maxPasajeros[0]['max_marcianos']
                    if (number_pasajeros_aeronave < cupoMaximo):
                        accion = 'crear'
                    else:
                        form.add_error('aeronave', 'El cupo limite ha sido alcanzado para esta aeronave')


        if form.is_valid():
            if(accion == 'crear'):
                form.save()
            elif(accion == 'actualizar'):
                GestionPasajeros.objects.filter(id=valueId).update(activo=valueActivo)

            return redirect('aeronave:pasajero_aeronaves_lista')
    else:
        form = GestionarPasajeroForm()

    return render(request, 'aeronave/aeronave_form.html', {'form':form})

def gestionpasajeros_lista(request):
    gestionPasajeros = GestionPasajeros.objects.all().filter(activo=1).order_by('id')
    contexto = {'gestionPasajeros': gestionPasajeros}
    return render(request, 'aeronave/listado_gestionpasajeros.html', contexto)

def aeronave_review(request,id_aeronave):
    aeronave = Aeronave.objects.get(id=id_aeronave)
    objetouno = GestionPasajeros.objects.filter(aeronave=id_aeronave, activo=True)

    fechadehoy = datetime.date.today()
    yarevisada = RegistroNaveRevisada.objects.filter(aeronave=id_aeronave, fecha=fechadehoy).exists()
    if (yarevisada):
        contexto = {'revisada': 'revisada'}
    else:
        if request.method == 'POST':
            form = ListadoRevisionNaveForm(request.POST)
            if form.is_valid():
                identificador = form.cleaned_data['identificador']
                nombre = form.cleaned_data['nombre']
                fecha = form.cleaned_data['fecha']
                for obj in objetouno:
                    idObjto = obj.id
                    objgpasajero = GestionPasajeros.objects.get(id=idObjto)
                    objtoregistro = ListadoRevisionNave(identificador=identificador, nombre=nombre, fecha=fecha,
                                                        gestionpasajeros=objgpasajero)
                    objtoregistro.save()
                    idPasajero = objgpasajero.pasajero_id
                    objgpasajero = Pasajero.objects.get(id=idPasajero)
                    historial = HistorialNaveRevisada(fecha=fecha, aeronave=aeronave, pasajero=objgpasajero,
                                                      identificador=identificador)
                    historial.save()
                objNaveRevisada = RegistroNaveRevisada(fecha=fecha, aeronave=aeronave)
                objNaveRevisada.save()

            return redirect('aeronave:aeronave_lista')
        else:
            form = ListadoRevisionNaveForm()

        contexto = {'form': form, 'objetounos': objetouno}


    return render(request, 'aeronave/aeronave_review_form.html', contexto)