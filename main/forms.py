from django import forms
from . import models

# Form for user registration
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

# Form for user login
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

# Form for creating a new RideShare ride
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
            "contact": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Contact"}
            ),
        }
