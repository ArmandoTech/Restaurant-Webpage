from django.shortcuts import render
from django.utils import timezone

from .models import Menu




def index(request):
    if request.method=="POST":
        message_name= request.POST['message_name']
        message_address= request.POST['message_address']
        message_cellphone= request.POST['message_cellphone']
        message_product= request.POST['message_product']
    else:
        return render(request, 'index.html', {})


def menu(request):
    return render(request, 'menu.html', {})

def about(request):
    return render(request, 'about.html', {})

def book(request):
    return render(request, 'book.html', {})

