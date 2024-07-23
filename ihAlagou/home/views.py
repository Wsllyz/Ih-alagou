from django.shortcuts import render
from django.http import JsonResponse
import requests



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
    response = requests.get('https://api.thingspeak.com/channels/2602561/feeds.json?api_key=4OW0Z91BKJ5U61ZT&results=2')
    if response.status_code == 200:
        dados = response.json()
        return JsonResponse({'dados':dados})
    return

def home_view(request):
    response = requests.get('https://api.thingspeak.com/channels/2602561/feeds.json?api_key=4OW0Z91BKJ5U61ZT&results=2')
    if response.status_code == 200:
        dados = response.json()
        return render(request, 'index.html', {'dados':dados})
    return render(request, 'index.html', {'dados':dados})
