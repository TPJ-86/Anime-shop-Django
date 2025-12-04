from django.shortcuts import render
from .models import Product, Category


def home(request):
    """Главная страница"""
    return render(request, 'home.html')

def products(request):
    """Страница всех товаров"""
    all_products = Product.objects.all() 
    return render(request, 'products.html', {'products': all_products})

def product_detail(request, id):
    """Страница одного товара"""
    try:
        product = Product.objects.get(id=id)  # Находим товар по ID
    except Product.DoesNotExist:
        # Если товар не найден - покажем 404
        from django.http import Http404
        raise Http404("Товар не найден")
    
    return render(request, 'product_detail.html', {'product': product})