from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductTemplateView, ProductDetailView
app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", ProductTemplateView.as_view(), name="contacts"),
    path("catalog/", ProductListView.as_view(), name="catalog"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product_detail")
]
