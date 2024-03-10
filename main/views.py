from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User as UserModel

from . import models
from . import forms



class RegisterView(View):
    def get(self, request):
        register_form = forms.register()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        register_form = forms.register(request.POST)
        if register_form.is_valid():
            first_name = register_form.cleaned_data["first_name"]
            last_name = register_form.cleaned_data["last_name"]
            email = register_form.cleaned_data["email"]
            password = register_form.cleaned_data["password"]
            confirm_password = register_form.cleaned_data["confirm_password"]
            if password == confirm_password:
                # Create UserModel
                user = UserModel.objects.create_user(
                    username=email, email=email, password=password
                )
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                return redirect("login")
            else:
                print("Password and Confirm Password does not match")
                return redirect("register")
        else:
            print(register_form.errors)
            return redirect("register")


class HomeView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "index-user.html", {"navbarActive": "home"})
        return render(request, "index.html", {"navbarActive": "home"})


