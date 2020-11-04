from django.shortcuts import render
from django.http import HttpRequest
from .models import Ingrediente, Menu, Piatto, IngredientePiatto, PiattoMenu


def index(req: HttpRequest):
    return render(req, 'menu/index.html')


def lista_ingredienti(req: HttpRequest):
    context = {'object_list': Ingrediente.objects.all().order_by('nome')}
    return render(req, 'menu/lista_ingredienti.html', context=context)


def lista_menu(req: HttpRequest):
    context = {'object_list': Menu.objects.all().order_by('nome')}
    return render(req, 'menu/lista_menu.html', context=context)


def lista_piatti(req: HttpRequest):
    piatti = Piatto.objects.all().order_by('nome')
    l = [(p, IngredientePiatto.objects.filter(piatto=p)) for p in piatti]
    context = {
        'object_list': l,
    }
    return render(req, 'menu/lista_piatti.html', context=context)


def dettaglio_menu(req : HttpRequest, id):
    menu = Menu.objects.filter(pk=id).first()
    lista_piatti = PiattoMenu.objects.filter(menu=menu)
    context = {'menu': menu, 'lista_piatti': lista_piatti}
    return render(req, 'menu/dettaglio_menu.html', context=context)
