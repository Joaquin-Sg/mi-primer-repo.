from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime

# Create your views here.

def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"hola mundo {fecha_hora_ahora}")
