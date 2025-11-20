from django.contrib import admin

from .models import Cafe


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "city",
        "area",
        "price_level",
        "rating",
        "is_open_now",
    )
    list_filter = (
        "city",
        "area",
        "price_level",
        "has_wifi",
        "has_food",
        "is_open_now",
    )
    search_fields = (
        "name",
        "slug",
        "tagline",
        "address",
        "features",
    )
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("-rating", "name")
