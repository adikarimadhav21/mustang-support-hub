from django.contrib import admin

from . import models

admin.site.site_header = '🐎 MSH administration'
admin.site.site_title = '🐎 MSH administration'
admin.site.index_title = '🐎 MSH administration'

@admin.register(models.MarketplaceCategoryModel)
class MarketplaceCategoryAdmin(admin.ModelAdmin):
    list_display = ["category"]


@admin.register(models.MarketplaceModel)
class MarketplacwAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "user", "price", "contact"]
    list_filter = ["category", "user"]


@admin.register(models.RoomFinderModel)
class RoomFinderAdmin(admin.ModelAdmin):
    list_display = ["title", "location", "no_of_availability", "contact"]
    list_filter = ["location"]


@admin.register(models.RideShareModel)
class RideShareAdmin(admin.ModelAdmin):
    list_display = [
        "start_location",
        "end_location",
        "datetime",
        "available_seats",
        "total_seats",
        "contact",
    ]
    list_filter = ["start_location", "end_location"]


@admin.register(models.LostAndFoundCategoryModel)
class LostAndFoundCategoryAdmin(admin.ModelAdmin):
    list_display = ["category"]


@admin.register(models.LostAndFoundModel)
class LostAndFoundAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "description", "contact"]
    list_filter = ["category"]


@admin.register(models.ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "created_at"]
    list_filter = ["created_at"]
