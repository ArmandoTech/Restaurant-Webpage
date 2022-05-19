from django.urls import URLPattern, path
from . import views

#app_name='pedidos'
urlpatterns = [
    path('', views.index, name='index'),
    path('menu.html', views.menu, name='menu'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('book.html', views.book, name='book'),
]
