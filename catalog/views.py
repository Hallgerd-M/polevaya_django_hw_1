from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from django.views.generic.edit import CreateView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product


class ProductTemplateView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:catalog")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:catalog")

    #   def get_object(self, queryset=None):
    #      self.object = super().get_object(queryset)
    #     if self.request.user == self.object.owner:
    #        return self.object
    #  raise PermissionDenied

    def get_form_class(self, queryset=None):
        user = self.request.user
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        elif user.is_superuser or self.request.user == self.object.owner:
            return ProductForm
        raise PermissionDenied


#    def get_success_url(self):
#        return reverse_lazy('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:catalog")

    def get_object(self, queryset=None):
        user = self.request.user
        product = super().get_object()
        if user != product.owner:
            raise PermissionDenied
