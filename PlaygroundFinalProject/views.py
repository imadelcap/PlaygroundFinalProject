from django.http import HttpResponse
from django.template import loader


def inicio(request):
    plantilla = loader.get_template("index.html")
    documento = plantilla.render()
    return HttpResponse(documento)