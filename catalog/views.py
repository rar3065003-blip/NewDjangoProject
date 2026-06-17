from django.shortcuts import render, get_object_or_404
from catalog.models import Product

def home_view(request):
    latest_products = Product.objects.all()
    print(latest_products)
    context = {'products': latest_products}
    return render(request, "catalog/home.html", context)


def contacts_view(request):
    return render(request, "catalog/contacts.html")


def product_detail(request, pk):
    """Контроллер для отображения детальной информации о товаре"""
    # Находим товар по его первичному ключу (id) или возвращаем ошибку 404
    product = get_object_or_404(Product, pk=pk)

    # Передаем объект товара в шаблон
    context = {
        'object': product  # В курсах часто называют переменную 'object' или 'product'
    }
    return render(request, 'catalog/product_detail.html', context)