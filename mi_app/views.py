from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Familia

# Create your views here.

def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"hola mundo {fecha_hora_ahora}")


def saludo_personalizado(request):
    context = {}

    if request.GET:
        context["nombre"] = request.GET["nombre"]

    return render(request, "mi_app/index.html", context)

def familia(request):
    context= {}

    context["familiar"] = Familia.objects.all()

    return render(request, "mi_app/familia.html", context)

