from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["contact_name", "es_id", "phone", "phone2", "email", "working_mode", "photo"]
    list_filter = ["contact_name"]