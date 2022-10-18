from array import array
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    template = loader.get_template('accueil.html')
    import datetime

    x = datetime.datetime.now()
    
    context = {
    'now': x,
    'nom': 'Souissi', # écrire votre nom ici
    'prenom':'Ahmed',
    'age':'20',
    'sexe':'F',
    'adresse':'AFH',
    'class':'dsi23',
    }
    return HttpResponse(template.render(context, request))

def consulter(request):
    template = loader.get_template('notes.html')
    import datetime
    x = datetime.datetime.now()
    context = {
        'nom': 'Souissi', # écrire votre nom ici
        'prenom':'Ahmed',
        'sexe':'F',
        'notes': [10, 0, 14, 16, 18],
        }
    return HttpResponse(template.render(context, request))
def retourner(request):
    return HttpResponseRedirect(reverse('index'))