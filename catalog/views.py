from django.views.generic import DetailView, ListView, TemplateView

from catalog.models import Product


class ProductTemplateView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
