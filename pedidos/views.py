from django.shortcuts import render
from django.utils import timezone

from .models import Menu


# def listMenus(request):
#     menu = Menu.objects.all()

#     context = {
#         'name': Menu.name
#     }

#     return render(request, 'pedidos/menu.html', context)

def index(request):
    return render(request, 'index.html', {})


def menu(request):
    return render(request, 'menu.html', {})


def about(request):
    return render(request, 'about.html', {})

def book(request):
    return render(request, 'book.html', {})











# class IndexView(generic.ListView):
#     template_name= 'pedidos/index.html'
    
#     def get_queryset(self):
#         return Pedido.objects.filter(fecha_pedido__lte=timezone.now())


