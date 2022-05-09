from django.urls import URLPattern, path
from . import views

app_name='pedidos'
urlpatterns = [
    path('', views.index, name='index'),
]
