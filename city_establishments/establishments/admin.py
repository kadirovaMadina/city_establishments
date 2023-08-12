from django.contrib import admin
from .models import Establishment

# Register your models here.

@admin.register(Establishment)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["es_name", "category", "type", "description", "address", "city"]
    list_filter = ["es_name", "category", "address", "city"]