from django.contrib import admin

from . import models

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
