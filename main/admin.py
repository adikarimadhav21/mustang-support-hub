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
