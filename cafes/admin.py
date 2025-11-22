from django.contrib import admin

from .models import Cafe, Favorite, Review


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


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "cafe", "created_at")
    search_fields = ("user__username", "cafe__name")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("cafe", "user", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("user__username", "cafe__name", "text")
