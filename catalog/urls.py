from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (ProductCreateView, ProductDeleteView,
                           ProductDetailView, ProductListView,
                           ProductTemplateView, ProductUpdateView,
                           CategoryDetailView, CategoryListView)

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", ProductTemplateView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="catalog"),
    path("catalog/", ProductListView.as_view(), name="catalog"),
    path("product/<int:pk>", cache_page(60 * 15)(ProductDetailView.as_view()), name="product_detail"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("catalog/categories", CategoryListView.as_view(), name="categories"),
    path("catalog/<int:pk>", CategoryDetailView.as_view(), name="products_by_category"),
]
