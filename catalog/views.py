from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView, UpdateView,  DeleteView
from django.views.generic.edit import CreateView
from catalog.forms import ProductForm
from django.urls import reverse_lazy


class ProductTemplateView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

#    def get_success_url(self):
#        return reverse_lazy('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:catalog')
