from django.db import models


class Post(models.Model):
    heading = models.CharField(
        max_length=100, verbose_name="Заголовок", help_text="Введите заголовок"
    )
    content = models.TextField(verbose_name="Содержимое", help_text="Введите текст")
    preview = models.ImageField(
        upload_to="blog/photos",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    created_at = models.DateField(auto_now_add=True)
    published_tag = models.BooleanField(default=True)
    views_counter = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = ["heading", "created_at"]
