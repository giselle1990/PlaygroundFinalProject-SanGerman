from django.shortcuts import render, HttpResponse
from .models import Producto
def tienda(request):
    return render(request, "tienda/tienda.html")



def tienda(request):
	
    productos=Producto.objects.all()

    return render (request, "tienda/tienda.html", {"productos": productos})