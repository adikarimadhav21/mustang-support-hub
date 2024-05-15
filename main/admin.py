from django.contrib import admin
from . import models

# Set the site header, title, and index title for the Django admin site
admin.site.site_header = '🐎 MSH administration'
admin.site.site_title = '🐎 MSH administration'
admin.site.index_title = '🐎 MSH administration'

# Register the Marketplace Category Model for admin management
@admin.register(models.MarketplaceCategoryModel)
class MarketplaceCategoryAdmin(admin.ModelAdmin):
    # Display the 'category' field in the admin list view
    list_display = ["category"]

# Register the Marketplace Model for admin management
@admin.register(models.MarketplaceModel)
class MarketplacwAdmin(admin.ModelAdmin):
    # Display selected fields in the admin list view
    list_display = ["title", "category", "user", "price", "contact"]
    # Add filters for the 'category' and 'user' fields in the admin list view
    list_filter = ["category", "user"]

# Register the Room Finder Model for admin management
@admin.register(models.RoomFinderModel)
class RoomFinderAdmin(admin.ModelAdmin):
    # Display selected fields in the admin list view
    list_display = ["title", "location", "no_of_availability", "contact"]
    # Add filters for the 'location' field in the admin list view
    list_filter = ["location"]

# Register the Ride Share Model for admin management
@admin.register(models.RideShareModel)
class RideShareAdmin(admin.ModelAdmin):
    # Display selected fields in the admin list view
    list_display = [
        "start_location",
        "end_location",
        "datetime",
        "available_seats",
        "total_seats",
        "contact",
    ]
    # Add filters for the 'start_location' and 'end_location' fields in the admin list view
    list_filter = ["start_location", "end_location"]

# Register the Lost and Found Category Model for admin management
@admin.register(models.LostAndFoundCategoryModel)
class LostAndFoundCategoryAdmin(admin.ModelAdmin):
    # Display the 'category' field in the admin list view
    list_display = ["category"]

# Register the Lost and Found Model for admin management
@admin.register(models.LostAndFoundModel)
class LostAndFoundAdmin(admin.ModelAdmin):
    # Display selected fields in the admin list view
    list_display = ["title", "category", "description", "contact"]
    # Add a filter for the 'category' field in the admin list view
    list_filter = ["category"]

# Register the Contact Model for admin management
@admin.register(models.ContactModel)
class ContactAdmin(admin.ModelAdmin):
    # Display selected fields in the admin list view
    list_display = ["name", "email", "subject", "created_at"]
    # Add a filter for the 'created_at' field in the admin list view
    list_filter = ["created_at"]
