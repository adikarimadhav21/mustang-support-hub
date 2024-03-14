from django import forms

from . import models


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


