from django.shortcuts import get_object_or_404, render
from .models import Category, Product

# Create your views here.
    
def product_all(request):
    products = Product.products.all()
    return render(request, 'tienda/home.html', {'products': products})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'tienda/productos/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'tienda/productos/producto.html', {'product': product})