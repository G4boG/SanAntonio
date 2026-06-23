from django.shortcuts import render, redirect
from .models import Escolar # Importamos la tabla que creamos
from .forms import EscolarForm



def listar_productos(request):
    # 1. Traemos la consulta base sin ejecutar
    #Lo que hace Django acá no es leer los 600 productos, sino que apunta solamente al contenedor de productos
    productos = Escolar.objects.all()
    
    # 2. CAPTURA DE PARÁMETROS DESDE LA URL (request.GET)
    busqueda = request.GET.get('q', '')         # Texto de la barra de búsqueda
    categoria = request.GET.get('cat', '')      # Filtro de categoría (el que ya creamos)
    ordenar_por = request.GET.get('order', '')  # Criterio de ordenamiento (precio, nombre)

    """ 
    El asistente mira la URL del navegador (request) para ver si el usuario escribió algo en la barra de búsqueda ('q'), si presionó un botón de categoría ('cat'), o si hizo clic en ordenar ('order').
    Si no hay nada, estas variables quedan vacías (''). 
    """


    # 3. APLICACIÓN DE FILTROS (Se van acumulando de forma inteligente)
    
    # Si el usuario escribió algo en la barra de búsqueda
    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)
        
    """ 
    Si el usuario escribió "Acuarela", el asistente busca en la caja de productos y saca solo los que contienen la palabra "acuarela" (sin importar mayúsculas o minúsculas por el __icontains), y descarta el resto. Ahora la caja quizás tiene solo 5 productos.
    """

    # Si el usuario seleccionó una categoría en la botonera
    if categoria:
        productos = productos.filter(categoria=categoria)
        
    """ 
    Si además el usuario tenía seleccionada la categoría "ESCOLAR", el asistente toma esos 5 productos que sobrevivieron al primer filtro y les aplica un segundo embudo. Si de las 5 acuarelas una era de "BAZAR", la quita. Los filtros se acumulan de forma inteligente.
    """

    # 4. APLICACIÓN DE ORDENAMIENTO (order_by)
    if ordenar_por == 'stock_asc':
        productos = productos.order_by('stock')       # Menor a Mayor
    elif ordenar_por == 'stock_desc':
        productos = productos.order_by('-stock')      # Mayor a Menor (el signo '-' invierte) 
    elif ordenar_por == 'nombre_az':
        productos = productos.order_by('nombre')       # A - Z
    elif ordenar_por == 'nombre_za':
        productos = productos.order_by('-nombre')      # Z - A

    # 5. EMPAQUETADO PARA EL TEMPLATE
    contexto = {
        'lista': productos,
        'busqueda_actual': busqueda, # Mantenemos el texto en la casilla para comodidad del usuario
        'categoria_actual': categoria,
        'orden_actual': ordenar_por
    }
    return render(request, 'SanAntonio/index.html', contexto)