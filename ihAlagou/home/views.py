from django.shortcuts import render
from .dynamo_client import get_items

# Create your views here.
def home_view(request):
    items = get_items()
    ultimoItem = items[-1]
    return render(request, 'index.html', {'items':ultimoItem})
