from django.shortcuts import render

# Create your views here.

__author__ = 'ines'

def index(request):
    context = { 'menu_order': ['quienes_somos', 'que_hacemos',
                               'circulo', 'galeria', 'articulos',
                               'contacto'],
                'menu': [
                    {'quienes_somos': '¿Quiénes somos?'},
                    {'que_hacemos': '¿Qué hacemos?'},
                    {'circulo': 'Círculo de Desarrollo Empresarial'},
                    {'galeria': 'Galería'},
                    {'articulos': 'Artículos'},
                    {'contacto': 'Contacto'}
                ]
    }
    return render(request, 'index.html', context)

