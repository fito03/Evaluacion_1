from django.shortcuts import render

# Create your views here.
def renderIndex(request):
    return render(request, 'templatesAPP1/index.html')

def renderProductos(request):
    return render(request, 'templatesAPP1/productos.html')