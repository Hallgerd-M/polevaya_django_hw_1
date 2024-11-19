from config.settings import CACHE_ENABLED
from django.core.cache import cache

from catalog.models import Product

def get_products_from_cache():
    """ Фукция, которая проверяет включен ли кеш, и в случае, если он включен,
     либо получает данные по продуктам из кеша, либо, если кеш пуст,
     получает данные из бд и загружает в кеш"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category):
    products = Product.objects.all()
    get_products_by_category = []
    for product in products:
        cat = Product.objects.get("category")
        if cat == category:
            get_products_by_category.append(product)
    return get_products_by_category
