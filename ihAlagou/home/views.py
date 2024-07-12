from django.shortcuts import render
from .dynamo_client import get_items
from django.http import JsonResponse


def pegaDistancia(dado):
    return {'distância': dado['payload']}

# Create your views 
def distancia_view(request):
    items = get_items()
    ultimoItem = items[-1]
    distancia = pegaDistancia(ultimoItem)
    distancia = distancia['distância']
    return JsonResponse({'distância': distancia['distância']})

def home_view(request):
    distancia = distancia_view(request)
    return render(request, 'index.html', {'distância':distancia})