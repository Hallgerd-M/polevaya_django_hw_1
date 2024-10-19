from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def catalog(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog.html", context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {"product": product}
    return render(request, 'product_detail.html', context)
