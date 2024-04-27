from . import models
from django.contrib import admin


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_filter = ["email"]
    search_fields = ["name", "email"]
    list_display = ["name", "email", "phone"]


@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_filter = ["buyer", "apartment"]
    list_display = ["buyer", "apartment", "from_date", "to_date", "total_price"]
