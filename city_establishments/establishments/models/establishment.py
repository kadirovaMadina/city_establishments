from django.db import models


class Establishment(models.Model):
    es_name = models.CharField("Название заведения", max_length=50)
    category = models.ForeignKey("categories.category", on_delete=models.CASCADE, related_name="establishments")
    type = models.ForeignKey("categories.type", on_delete=models.CASCADE, related_name="establishments")
    description = models.TextField("Описание заведения")
    address = models.CharField("Адрес заведения(улица и номер)", max_length=30)
    city = models.CharField("Город", max_length=25)

    class Meta:
        verbose_name = "Заведение"
        verbose_name_plural = "Заведения"

    def __str__(self):
        return f"{self.es_name}"