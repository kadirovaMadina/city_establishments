from django.db import models


class Contact(models.Model):
    contact_name = models.CharField("Имя контакта", max_length=50)
    es_id = models.OneToOneField("establishments.establishment", on_delete=models.CASCADE, related_name="contacts")
    phone = models.CharField("Номер телефона", max_length=30)
    phone2 = models.CharField("Дополнительный номер телефона", max_length=30)
    email = models.EmailField("Почта", unique=True)
    working_mode = models.CharField("Режим работы", max_length=50)
    photo = models.ImageField("Фотографии", upload_to="contacts/photo", null=True, blank=True)


    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.contact_name}"