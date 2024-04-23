from django import forms
from django.core.exceptions import ValidationError
import re

from . import models

# Define choice options for various form fields

GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Doesn't Matter", "Doesn't Matter"),
]

STAY_TYPE_CHOICES = [
    ("Short Term", "Short Term"),
    ("Long Term", "Long Term"),
    ("Doesn't Matter", "Doesn't Matter"),
]

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

# Custom validation functions

def validate_password(value):
    if len(value) < 8:
        raise ValidationError("Password should be at least 8 characters long")
    if not re.search(r"[A-Z]", value):
        raise ValidationError("Password should contain at least one uppercase letter")
    if not re.search(r"\W", value):
        raise ValidationError("Password should contain at least one special character")


def validate_email_domain(value):
    if not value.endswith("@my.msutexas.edu"):
        raise ValidationError("Email must end with '@my.msutexas.edu'")

# Form classes
class register(forms.Form):
    first_name = forms.CharField(
        label="First Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Your First Name...",
                "class": "form-control form-control-user",
            }
        ),
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Your Last Name...",
                "class": "form-control form-control-user",
            }
        ),
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        validators=[validate_email_domain],
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter Email Address...",
                "class": "form-control form-control-user",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        max_length=100,
        required=True,
        validators=[validate_password],
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control form-control-user",
            }
        ),
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control form-control-user",
            }
        ),
    )

#login form
class login(forms.Form):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter Email Address...",
                "class": "form-control form-control-user",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control form-control-user",
            }
        ),
    )


class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter Email Address...",
                "class": "form-control form-control-user",
            }
        ),
    )
    new_password = forms.CharField(
        label="New Password",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "New Password",
                "class": "form-control form-control-user",
            }
        ),
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm New Password",
                "class": "form-control form-control-user",
            }
        ),
    )


class MarketplaceForm(forms.ModelForm):
    class Meta:
        model = models.MarketplaceModel
        fields = [
            "category",
            "title",
            "description",
            "price",
            "image",
            "image_2",
            "image_3",
            "image_4",
            "contact",
        ]
        widgets = {
            "category": forms.Select(
                attrs={"class": "form-control", "placeholder": "Select Category"}
            ),
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Title"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter Description"}
            ),
            "price": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter Price"}
            ),
            "image": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Additional Image"}
            ),
            "image_2": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Additional Image"}
            ),
            "image_3": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Additional Image"}
            ),
            "image_4": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Additional Image"}
            ),
            "contact": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Contact"}
            ),
        }


class RoomFinderForm(forms.ModelForm):
    class Meta:
        model = models.RoomFinderModel
        fields = [
            "title",
            "description",
            "location",
            "no_of_availability",
            "image",
            "image_2",
            "image_3",
            "image_4",
            "contact",
            "available_from",
            "room_type",
            "prefered_gender",
            "stay_type",
            "smoking_preference",
            "vegetarian_preference",
            "pet_preference",
            "alcohol_preference",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Title"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter Description"}
            ),
            "location": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Location"}
            ),
            "no_of_availability": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter Availability"}
            ),
            "image": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Image"}
            ),
            "image_2": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Additional Image"}
            ),
            "image_3": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Additional Image"}
            ),
            "image_4": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Additional Image"}
            ),
            "contact": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Contact"}
            ),
            "available_from": forms.TextInput(attrs={"type": "date"}),
            "room_type": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Room Type"}
            ),
            "prefered_gender": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Select Prefered Gender",
                },
                choices=GENDER_CHOICES,
            ),
            "stay_type": forms.Select(
                attrs={"class": "form-control", "placeholder": "Select Stay Type"},
                choices=STAY_TYPE_CHOICES,
            ),
            "smoking_preference": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Select Smoking Preference",
                },
                choices=SMOKING_PREFERENCE_CHOICES,
            ),
            "vegetarian_preference": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Select Vegetarian Preference",
                },
                choices=VEGETARIAN_PREFERENCE_CHOICES,
            ),
            "pet_preference": forms.Select(
                attrs={"class": "form-control", "placeholder": "Select Pet Preference"},
                choices=PET_PREFERENCE_CHOICES,
            ),
            "alcohol_preference": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Select Alcohol Preference",
                },
                choices=ALCOHOL_PREFERENCE_CHOICES,
            ),
        }


class RideShareForm(forms.ModelForm):
    class Meta:
        model = models.RideShareModel
        fields = [
            "start_location",
            "end_location",
            "datetime",
            "description",
            "available_seats",
            "total_seats",
            "image",
            "image_2",
            "image_3",
            "image_4",
            "contact",
        ]
        widgets = {
            "start_location": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Start Location"}
            ),
            "end_location": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter End Location"}
            ),
            "datetime": forms.TextInput(attrs={"type": "datetime-local"}),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter Description"}
            ),
            "available_seats": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter Available Seats"}
            ),
            "total_seats": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter Total Seats"}
            ),
            "image": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Image"}
            ),
            "image_2": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Additional Image"}
            ),
            "image_3": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Additional Image"}
            ),
            "image_4": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Additional Image"}
            ),
            "contact": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Contact"}
            ),
        }


class LostAndFoundForm(forms.ModelForm):
    class Meta:
        model = models.LostAndFoundModel
        fields = [
            "title",
            "category",
            "description",
            "image",
            "image_2",
            "image_3",
            "image_4",
            "contact",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Title"}
            ),
            "category": forms.Select(
                attrs={"class": "form-control", "placeholder": "Select Category"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter Description"}
            ),
            "image": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Image"}
            ),
            "image_2": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Additional Image"}
            ),
            "image_3": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Additional Image"}
            ),
            "image_4": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Additional Image"}
            ),
            "contact": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Contact"}
            ),
        }


class UserProfileEditForm(forms.Form):
    first_name = forms.CharField(
        label="First Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Your First Name...",
                "class": "form-control form-control-user",
            }
        ),
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Your Last Name...",
                "class": "form-control form-control-user",
            }
        ),
    )


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.ContactModel
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter Email"}
            ),
            "subject": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Subject"}
            ),
            "message": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter Message"}
            ),
        }
