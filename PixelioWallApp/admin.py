from django.contrib import admin
from .models import CustomUser, Image, Favourite

# Register your models here.
# admin.site.register(CustomUser)
# admin.site.register(Image)
# admin.site.register(Favourite)

# ---------- CustomUser ----------
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "selected_theme", "profile_picture", "favourite_count")
    search_fields = ("username", "email")

    def favourite_count(self, obj):
        return obj.favourites.count()
    favourite_count.short_description = "Total Favourites"


# ---------- Image ----------
class ImageAdmin(admin.ModelAdmin):
    list_display = ("image_title", "category", "author", "is_paid", "image_price", "created_at")
    search_fields = ("image_title", "category", "author")
    list_filter = ("is_paid", "category", "created_at")


# ---------- Favourite ----------
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ("user", "get_image_title", "get_image_category", "get_is_paid", "created_at")
    search_fields = ("user__username", "image__image_title", "image__category")
    list_filter = ("created_at", "image__is_paid")

    def get_image_title(self, obj):
        return obj.image.image_title
    get_image_title.short_description = "Image Title"

    def get_image_category(self, obj):
        return obj.image.category
    get_image_category.short_description = "Category"

    def get_is_paid(self, obj):
        return obj.image.is_paid
    get_is_paid.short_description = "Paid?"


# ---------- Register all ----------
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Favourite, FavouriteAdmin)
