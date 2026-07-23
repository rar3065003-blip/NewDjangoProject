from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView

from catalog.models import Product


class HomeView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


# def home_view(request):
#     latest_products = Product.objects.all()
#     print(latest_products)
#     context = {'products': latest_products}
#     return render(request, "catalog/home.html", context)


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


# def contacts_view(request):
#     return render(request, "catalog/contacts.html")


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


def product_detail(request, pk):
    """Контроллер для отображения детальной информации о товаре"""
    # Находим товар по его первичному ключу (id) или возвращаем ошибку 404
    product = get_object_or_404(Product, pk=pk)

    # Передаем объект товара в шаблон
    context = {
        "object": product  # В курсах часто называют переменную 'object' или 'product'
    }
    return render(request, "catalog/product_detail.html", context)
