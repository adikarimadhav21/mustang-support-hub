from django.db import models
from django.contrib.auth.models import User

#roomfinder form option 
GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Doesn't Matter", "Doesn't Matter"),
]
#roomfinder form option 

STAY_TYPE_CHOICES = [
    ("Short Term", "Short Term"),
    ("Long Term", "Long Term"),
    ("Doesn't Matter", "Doesn't Matter"),
]
#roomfinder form option 

SMOKING_PREFERENCE_CHOICES = [
    ("Non-Smoker", "Non-Smoker"),
    ("Outside Only", "Outside Only"),
    ("Doesn't Matter", "Doesn't Matter"),
]

VEGETARIAN_PREFERENCE_CHOICES = [
    ("Vegetarian", "Vegetarian"),
    ("Non-Vegetarian", "Non-Vegetarian"),
    ("Doesn't Matter", "Doesn't Matter"),
]

PET_PREFERENCE_CHOICES = [
    ("No Pets", "No Pets"),
    ("Doesn't Matter", "Doesn't Matter"),
]

ALCOHOL_PREFERENCE_CHOICES = [
    ("No Alcohol", "No Alcohol"),
    ("Doesn't Matter", "Doesn't Matter"),
]

#module for marketplace category
class MarketplaceCategoryModel(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Marketplace Category"
        verbose_name_plural = "Marketplace Categories"

#module for marketplace
class MarketplaceModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(MarketplaceCategoryModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="marketplace")
    image_2 = models.ImageField(upload_to="marketplace", blank=True, null=True)
    image_3 = models.ImageField(upload_to="marketplace", blank=True, null=True)
    image_4 = models.ImageField(upload_to="marketplace", blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    contact = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Marketplace Item"
        verbose_name_plural = "Marketplace Items"

#module for room finder
class RoomFinderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="room_finder")
    image_2 = models.ImageField(upload_to="room_finder", blank=True, null=True)
    image_3 = models.ImageField(upload_to="room_finder", blank=True, null=True)
    image_4 = models.ImageField(upload_to="room_finder", blank=True, null=True)
    location = models.CharField(max_length=100)
    no_of_availability = models.IntegerField()
    available_from = models.DateField()
    room_type = models.CharField(max_length=100)
    prefered_gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    stay_type = models.CharField(max_length=20, choices=STAY_TYPE_CHOICES)
    smoking_preference = models.CharField(
        max_length=20, choices=SMOKING_PREFERENCE_CHOICES
    )
    vegetarian_preference = models.CharField(
        max_length=20, choices=VEGETARIAN_PREFERENCE_CHOICES
    )
    pet_preference = models.CharField(max_length=20, choices=PET_PREFERENCE_CHOICES)
    alcohol_preference = models.CharField(
        max_length=20, choices=ALCOHOL_PREFERENCE_CHOICES
    )
    contact = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Room Finder"
        verbose_name_plural = "Room Finders"

# Model for ride sharing information
class RideShareModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(upload_to="ride_share")
    image_2 = models.ImageField(upload_to="ride_share", blank=True, null=True)
    image_3 = models.ImageField(upload_to="ride_share", blank=True, null=True)
    image_4 = models.ImageField(upload_to="ride_share", blank=True, null=True)
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

# Model for lost and found item categories
class LostAndFoundCategoryModel(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Lost and Found Category"
        verbose_name_plural = "Lost and Found Categories"

# Model for lost and found item 
class LostAndFoundModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(LostAndFoundCategoryModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="lost_and_found")
    image_2 = models.ImageField(upload_to="lost_and_found", blank=True, null=True)
    image_3 = models.ImageField(upload_to="lost_and_found", blank=True, null=True)
    image_4 = models.ImageField(upload_to="lost_and_found", blank=True, null=True)
    contact = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Lost and Found"
        verbose_name_plural = "Lost and Founds"

# Model for contact
class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
