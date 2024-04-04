from django.db import models
from django.contrib.auth.models import User

class RideShareModel(models.Model):
    # User who created the ride
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Start and end locations of the ride
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    
    # Date and time of the ride
    datetime = models.DateTimeField()
    
    # Description of the ride
    description = models.TextField()
    
    # Number of available seats in the ride
    available_seats = models.IntegerField()
    
    # Total number of seats in the ride
    total_seats = models.IntegerField()
    
    # Contact information for the ride
    contact = models.CharField(max_length=100)
    
    # Date and time when the ride was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Date and time when the ride was last updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.start_location + " to " + self.end_location

    class Meta:
        verbose_name = "Ride Share"
        verbose_name_plural = "Ride Shares"


#model for room finder 
class RoomFinderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    no_of_availability = models.IntegerField()
    contact = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Room Finder"
        verbose_name_plural = "Room Finders"
