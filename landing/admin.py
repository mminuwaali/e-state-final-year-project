from . import models
from django.contrib import admin


class ImageInline(admin.TabularInline):
    extra, model = 1, models.Image


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "created_at", "updated_at"]


@admin.register(models.Apartment)
class apartmentAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_filter = ["category", "owner"]
    search_fields = ["name", "owner__username"]
    list_display = ["name", "owner", "price", "category"]
