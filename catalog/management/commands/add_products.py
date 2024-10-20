from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(
            name="Кофе", description="Бодрящий напиток с кофеином"
        )

        products = [
            {
                "name": "Арабика в зернах",
                "description": "Зерновой кофе арабика премиум",
                "category": category,
                "price": 10,
                "created_at": "2024-10-07",
                "updated_at": "2024-10-07",
            },
            {
                "name": "Арабика молотая",
                "description": "Молотый кофе арабика премиум",
                "category": category,
                "price": 20,
                "created_at": "2024-10-07",
                "updated_at": "2024-10-07",
            },
            {
                "name": "Робуста в зернах",
                "description": "Зерновой кофе робуста",
                "category": category,
                "price": 5,
                "created_at": "2024-10-07",
                "updated_at": "2024-10-07",
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Product {product.name} added successfully")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Product {product.name} already exists")
                )
