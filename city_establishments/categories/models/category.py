from django.db import models


class Category(models.Model):
    name = models.CharField("Название категории", max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"