from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, catalog, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("catalog/", catalog, name="catalog"),
    path("product/<int:id>", product_detail, name="product_detail")
]
