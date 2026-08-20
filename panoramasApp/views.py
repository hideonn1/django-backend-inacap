from django.shortcuts import render

VEHICULOS = [
    'Ford Mustang',
    'Chevrolet Camaro',
    'Dodge Challenger',
    'Nissan GT-R',
    'Toyota Supra',
]
PELICULAS = [
    'La vida es bella',
    'El padrino',
    'El gran dictador',
    'El código da Vinci',
    'El amor en los tiempos del cólera',
]
LIBROS = [
    'Cien años de soledad',
    'Quijote de la Mancha',
    'El principito',
    'El código da Vinci',
    'El amor en los tiempos del cólera',
]


def index(request):
    data = {
        'titulo': 'Bienvenido a Panoramas',
    }
    return render(request, 'index.html', data)


def _catalogo(request, pagina, titulo, tipo, catalogo):
    q = (request.GET.get('q') or '').strip()
    if q:
        items = [item for item in catalogo if q.lower() in item.lower()]
    else:
        items = catalogo
    data = {
        'titulo': titulo,
        'pagina': pagina,
        'tipo': tipo,
        'q': q,
        'catalogo': catalogo,
        'items': items,
    }
    return render(request, 'base.html', data)


def vehiculos(request):
    return _catalogo(request, 'vehiculos', 'Vehiculos', 'Un vehiculo', VEHICULOS)


def peliculas(request):
    return _catalogo(request, 'peliculas', 'Peliculas', 'Una pelicula', PELICULAS)


def libros(request):
    return _catalogo(request, 'libros', 'Libros', 'Un libro', LIBROS)
