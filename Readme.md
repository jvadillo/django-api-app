
# Tutorial: Cómo exponer datos de un modelo Django en formato JSON (sin frameworks externos)

Este tutorial te guía paso a paso para ofrecer los datos de un modelo Django en formato JSON utilizando solamente Django.

---

## Paso 0: Crear un nuevo proyecto y aplicación

### 0.1 Crear el proyecto

```bash
django-admin startproject myproject
cd myproject
```

### 0.2 Crear una aplicación

```bash
python manage.py startapp apiapp
```

### 0.3 Registrar la aplicación en `settings.py`

```python
# myproject/settings.py

INSTALLED_APPS = [
    # ...
    'apiapp',
]
```

---

## Paso 1: Definir el modelo

En `countries/models.py`, define el modelo `Country`:

```python
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    population = models.BigIntegerField()

    def __str__(self):
        return self.name
```

---

## Paso 2: Crear y aplicar las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Paso 3: Crear la vista que devuelve JSON

En `apiapp/views.py`, agrega lo siguiente:

```python
from django.http import JsonResponse
from .models import Country

def country_list(request):
    countries = Country.objects.all().values('name', 'capital', 'population')
    data = list(countries)  # Convertimos el QuerySet en una lista de diccionarios
    return JsonResponse(data, safe=False)
```

> 🔍 `safe=False` permite devolver una lista en lugar de un diccionario.

---

## Paso 4: Agregar la URL

En `apiapp/urls.py` (créalo si no existe):

```python
from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.country_list, name='country_list'),
]
```

Y en `myproject/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apiapp.urls')),
]
```

---

## Paso 5: Probar en el navegador

Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

Abre tu navegador en:

```
http://localhost:8000/countries/
```

Deberías ver una salida similar a esta (tendrás que introducir datos en la base de datos mediante shell o la aplicación del administrador):

```json
[
  {
    "name": "Kenya",
    "capital": "Nairobi",
    "population": 53771300
  },
  {
    "name": "Poland",
    "capital": "Warsaw",
    "population": 37950802
  }
]
```

---

¡Listo! Has expuesto datos de un modelo Django en JSON sin usar frameworks externos.
