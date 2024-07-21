from django.shortcuts import render
from django.http import JsonResponse


def pegaDistancia(dado):
    return {'distância': dado['payload']}

'''
def distancia_view(request):
    items = get_items()
    ultimoItem = items[-1]
    distancia = pegaDistancia(ultimoItem)
    distancia = distancia['distância']
    return JsonResponse({'distância': distancia['distância']})
'''

def distancia_view(request):
    pass
    return '2'

def home_view(request):
    '''
    items = get_items()
    ultimoItem = items[-1]
    distancia = pegaDistancia(ultimoItem)
    distancia = distancia['distância']
    '''
    return render(request, 'index.html')