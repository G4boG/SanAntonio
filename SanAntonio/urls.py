from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='lista_prods')
]