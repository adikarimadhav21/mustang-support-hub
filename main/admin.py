from django.contrib import admin
from . import models

# Registering RideShareModel with the admin site
@admin.register(models.RideShareModel)
class RideShareAdmin(admin.ModelAdmin):
    # Displaying these fields as columns in the admin list view
    list_display = [
        "start_location",
        "end_location",
        "datetime",
        "available_seats",
        "total_seats",
        "contact",
    ]
    
    # Adding filters to the admin list view
    list_filter = ["start_location", "end_location"]

# Registering RoomFinderModel with the admin site

@admin.register(models.RoomFinderModel)
class RoomFinderAdmin(admin.ModelAdmin):
    list_display = ["title", "location", "no_of_availability", "contact"]
    list_filter = ["location"]

@admin.register(models.MarketplaceCategoryModel)
class MarketplaceCategoryAdmin(admin.ModelAdmin):
    list_display = ["category"]


@admin.register(models.MarketplaceModel)
class MarketplacwAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "user", "price", "contact"]
    list_filter = ["category", "user"]
