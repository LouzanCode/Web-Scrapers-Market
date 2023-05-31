from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .carrito import Carrito
from tienda.models import Product

# Create your views here.
def carrito_total(request):
    carrito = Carrito(request)
    return render(request, 'tienda/carrito/total.html', {'carrito': carrito})

def carrito_add(request):
    carrito = Carrito(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        carrito.add(product=product)
        response = JsonResponse({'test': 'data'})
        return response

def carrito_delete(request):
    carrito = Carrito(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        carrito.delete(product=product_id)
        carritototal = carrito.get_total_price()
        response = JsonResponse({'Success': True, 'total': carritototal})
        return response