from django.db import models
from django.contrib.auth.models import User


class RideShareModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    description = models.TextField()
    available_seats = models.IntegerField()
    total_seats = models.IntegerField()
    contact = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.start_location + " to " + self.end_location

    class Meta:
        verbose_name = "Ride Share"
        verbose_name_plural = "Ride Shares"