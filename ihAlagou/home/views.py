from django.shortcuts import render
from .dynamo_client import get_items


def pegaDistancia(dado):
    if 'distância' in dado:
        return {'distância': dado['distância']}
    return 'aaaa'

# Create your views here.
def home_view(request):
    items = get_items()
    ultimoItem = items[-1]
    distância = ultimoItem
    return render(request, 'index.html', {'distância':distância})

