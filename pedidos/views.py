from django.shortcuts import render
from django.utils import timezone
from django.core.mail import send_mail

from .models import Menu




def index(request):
    if request.method=="POST":
        message_name= request.POST['message_name']
        message_address= request.POST['message_address']
        message_cellphone= request.POST['message_cellphone']
        message_product= request.POST['message_product']
        message_email= request.POST['message_email']
        message_date= request.POST['message_date']

        final_message=f'DIRECCION: {message_address}, CELULAR: {message_cellphone}, PRODUCTO: {message_product}, FECHA: {message_date}'

        send_mail(
            'NUEVO PEDIDO DE: ' + message_name,
            final_message,
            message_email,
            ['americangrillbga@gmail.com']
            )

        return render(request, 'index.html', {'message_name': message_name})
    else:
        return render(request, 'index.html', {})


def menu(request):
    return render(request, 'menu.html', {})

def about(request):
    return render(request, 'about.html', {})

def book(request):
    if request.method=="POST":
        message_name= request.POST['message_name']
        message_address= request.POST['message_address']
        message_cellphone= request.POST['message_cellphone']
        message_product= request.POST['message_product']
        message_email= request.POST['message_email']
        message_date= request.POST['message_date']

        final_message=f'DIRECCION: {message_address}, CELULAR: {message_cellphone}, PRODUCTO: {message_product}, FECHA: {message_date}'

        send_mail(
            'NUEVO PEDIDO DE: ' + message_name,
            final_message,
            message_email,
            ['americangrillbga@gmail.com']
            )

        return render(request, 'book.html', {'message_name': message_name})
    else:
        return render(request, 'book.html', {})

