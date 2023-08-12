from django.db import models


class Type(models.Model):
    name = models.CharField("Название типа заведения", max_length=50)
    category = models.ForeignKey("categories.category", on_delete=models.CASCADE, related_name="types")

    class Meta:
        verbose_name = "Тип заведения"
        verbose_name_plural = "Типы заведений"

    def __str__(self):
        return f"{self.name}"