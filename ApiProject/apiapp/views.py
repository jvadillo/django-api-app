from django.http import JsonResponse
from .models import Country

def country_list(request):
    countries = Country.objects.all().values('name', 'capital', 'population')
    data = list(countries)  # Convertimos el QuerySet en lista de diccionarios
    return JsonResponse(data, safe=False) # safe=False es necesario porque por defecto JsonResponse solo acepta diccionarios, pero aquí estamos devolviendo una lista.