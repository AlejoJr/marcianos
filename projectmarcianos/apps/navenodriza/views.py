from django.shortcuts import render

# Create your views here.
def navenodriza_lista(request):
    return render(request, 'navenodriza/listado_navesnodriza.html', {})