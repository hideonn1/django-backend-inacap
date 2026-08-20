from django.shortcuts import render

# Create your views here.
def index(request):
    data= {
        'titulo': 'Bienvenido a Panoramas',
    }
    return render(request, 'index.html', data)

def vehiculos(request):
    data= {
        'titulo': 'Vehiculos',
        'pagina': 'vehiculos',
        'tipo': 'Un vehiculo',
        'valor1': 'Ford Mustang',
        'valor2': 'Chevrolet Camaro',
        'valor3': 'Dodge Challenger',
        'valor4': 'Nissan GT-R',
        'valor5': 'Toyota Supra',
    }
    return render(request, 'base.html', data)

def peliculas(request):
    data= {
        'titulo': 'Peliculas',
        'pagina': 'peliculas',
        'tipo': 'Una pelicula',
        'valor1': 'La vida es bella',
        'valor2': 'El padrino',
        'valor3': 'El gran dictador',
        'valor4': 'El código da Vinci',
        'valor5': 'El amor en los tiempos del cólera',
    }
    return render(request, 'base.html', data)

def libros(request):
    data= {
        'titulo': 'Libros',
        'pagina': 'libros',
        'tipo': 'Un libro',
        'valor1': 'Cien años de soledad',
        'valor2': 'Quijote de la Mancha',
        'valor3': 'El principito',
        'valor4': 'El código da Vinci',
        'valor5': 'El amor en los tiempos del cólera',
    }
    return render(request, 'base.html', data)