from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Наименование", help_text="Введите наименование"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Наименование", help_text="Введите наименование"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание"
    )
    image = models.ImageField(
        upload_to="catalog/photos",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.IntegerField(verbose_name="", help_text="")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    publication_status = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="Введите сладельца продукта",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["category", "name"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
