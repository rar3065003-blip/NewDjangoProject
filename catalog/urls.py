from django.urls import path

from .views import (
    ContactsView,
    HomeView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
)

app_name = "catalog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("create/", ProductCreateView.as_view(), name="create_product"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="update_product"),
]
