from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User as UserModel

from . import models
from . import forms

# View for logging out the user
def LogoutView(request):
    logout(request)
    return redirect("login")

# View for user login
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        login_form = forms.login()
        return render(request, "login.html", {"login_form": login_form})

    def post(self, request):
        login_form = forms.login(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data["email"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                print("Invalid Credentials")
                return redirect("login")

# View for user registration
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

# View for the home page
class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "index-user.html", {"navbarActive": "home"})
        return render(request, "index.html", {"navbarActive": "home"})

# View for the RideShare page
class RideShareView(View):
    def get(self, request):
        if request.user.is_authenticated:
            rideshare_items = models.RideShareModel.objects.all().order_by(
                "-created_at"
            )
            return render(
                request,
                "rideshare-user.html",
                {"navbarActive": "rideshare", "rideshare_items": rideshare_items},
            )
        return render(request, "rideshare.html", {"navbarActive": "rideshare"})

# View for a specific RideShare ride
class RideShareRideView(View):
    def get(self, request, pk):
        rideshare_item = models.RideShareModel.objects.get(pk=pk)
        return render(
            request,
            "rideshare-ride.html",
            {
                "navbarActive": "rideshare",
                "rideshare_item": rideshare_item,
            },
        )

# View for creating a new RideShare ride
class RideShareRideNewView(View):
    def get(self, request):
        if request.user.is_authenticated:
            rideshare_ride_form = forms.RideShareForm()
            return render(
                request,
                "rideshare-ride-new.html",
                {
                    "navbarActive": "rideshare",
                    "rideshare_ride_form": rideshare_ride_form,
                },
            )
        return redirect("login")

    def post(self, request):
        rideshare_item_form = forms.RideShareForm(request.POST)
        if rideshare_item_form.is_valid():
            start_location = rideshare_item_form.cleaned_data["start_location"]
            end_location = rideshare_item_form.cleaned_data["end_location"]
            datetime = rideshare_item_form.cleaned_data["datetime"]
            description = rideshare_item_form.cleaned_data["description"]
            available_seats = rideshare_item_form.cleaned_data["available_seats"]
            total_seats = rideshare_item_form.cleaned_data["total_seats"]
            contact = rideshare_item_form.cleaned_data["contact"]
            user = request.user
            rideshare_item = models.RideShareModel(
                start_location=start_location,
                end_location=end_location,
                datetime=datetime,
                description=description,
                available_seats=available_seats,
                total_seats=total_seats,
                contact=contact,
                user=user,
            )
            rideshare_item.save()
            return redirect("rideshare")
        else:
            print(rideshare_item_form.errors)
            return render(
                request,
                "rideshare-ride-new.html",
                {
                    "navbarActive": "rideshare",
                    "rideshare_item_form": rideshare_item_form,
                    "error": rideshare_item_form.errors,
                },
            )
