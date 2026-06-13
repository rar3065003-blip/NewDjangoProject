from django.shortcuts import render
from catalog.models import Product

def home_view(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    print(latest_products)
    return render(request, "catalog/home.html")


def contacts_view(request):
    return render(request, "catalog/contacts.html")
