from django.shortcuts import render
from .dynamo_client import get_items
from django.http import JsonResponse


def pegaDistancia(dado):
    if 'payload' in dado:
        return {'distância': dado['payload']}
    return 'aaaa'

# Create your views 
def home_view(request):
    items = get_items()
    ultimoItem = items[-1]
    distancia = pegaDistancia(ultimoItem)
    distancia = distancia['distância']
    lesgo = distancia['distância']
    return render(request, 'index.html', {'distância':lesgo})

