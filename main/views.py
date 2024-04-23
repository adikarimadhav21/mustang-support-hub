from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User as UserModel
from django.db import IntegrityError
from django.contrib import messages

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
                messages.error(request, "Invalid Credentials")
                return redirect("login")

# View for user registration
class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
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
                try:
                    # Create UserModel
                    user = UserModel.objects.create_user(
                        username=email, email=email, password=password
                    )
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()

                    messages.success(request, "User created successfully")
                    return redirect("login")
                except IntegrityError:
                    register_form.add_error(
                        None, "Username already exists. Please choose a different one."
                    )
            else:
                register_form.add_error(
                    None, "Password and Confirm Password does not match"
                )
        else:
            print(register_form.errors)
            return render(
                request,
                "register.html",
                {"register_form": register_form, "error": register_form.errors},
            )
        return render(request, "register.html", {"register_form": register_form})


# View for password reset

class PasswordResetView(View):
    def get(self, request):
        password_reset_form = forms.PasswordResetForm()
        return render(
            request, "password-reset.html", {"password_reset_form": password_reset_form}
        )

    def post(self, request):
        password_reset_form = forms.PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            email = password_reset_form.cleaned_data["email"]
            user = UserModel.objects.get(email=email)
            password = password_reset_form.cleaned_data["new_password"]
            confirm_password = password_reset_form.cleaned_data["confirm_password"]
            if password == confirm_password:
                user.set_password(password)
                user.save()
                messages.success(request, "Password reset successfully")
                return redirect("login")
            else:
                password_reset_form.add_error(
                    None, "Password and Confirm Password does not match"
                )
        else:
            print(password_reset_form.errors)
            return render(
                request,
                "password-reset.html",
                {
                    "password_reset_form": password_reset_form,
                    "error": password_reset_form.errors,
                },
            )

# View for user profile edit

class ProfileEditView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            profile_edit_form = forms.UserProfileEditForm(
                initial={
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                }
            )
            return render(
                request,
                "user-profile-edit.html",
                {"profile_edit_form": profile_edit_form},
            )
        return redirect("login")

    def post(self, request):
        profile_edit_form = forms.UserProfileEditForm(request.POST)
        if profile_edit_form.is_valid():
            first_name = profile_edit_form.cleaned_data["first_name"]
            last_name = profile_edit_form.cleaned_data["last_name"]
            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect("home")
        else:
            print(profile_edit_form.errors)
            return redirect("profile_edit")


# View for home page
class HomeView(View):

    def get(self, request):
        if request.user.is_authenticated:
            marketplace_items = models.MarketplaceModel.objects.all().order_by(
                "-created_at"
            )[:4]
            roomfinder_items = models.RoomFinderModel.objects.all().order_by(
                "-created_at"
            )[:4]
            rideshare_items = models.RideShareModel.objects.all().order_by(
                "-created_at"
            )[:4]
            lostfound_items = models.LostAndFoundModel.objects.all().order_by(
                "-created_at"
            )[:4]
            return render(
                request,
                "index-user.html",
                {
                    "navbarActive": "home",
                    "marketplace_items": marketplace_items,
                    "roomfinder_items": roomfinder_items,
                    "rideshare_items": rideshare_items,
                    "lostfound_items": lostfound_items,
                },
            )
        return render(request, "index.html", {"navbarActive": "home"})

# View for marketplace

class MarketplaceView(View):
    def get(self, request):
        if request.user.is_authenticated:
            marketplace_items = models.MarketplaceModel.objects.all().order_by(
                "-created_at"
            )
            categories = models.MarketplaceCategoryModel.objects.all()
            return render(
                request,
                "marketplace-user.html",
                {
                    "navbarActive": "marketplace",
                    "marketplace_items": marketplace_items,
                    "categories": categories,
                },
            )
        return render(request, "marketplace.html", {"navbarActive": "marketplace"})


class UserMarketplaceView(View):
    def get(self, request):
        if request.user.is_authenticated:
            marketplace_items = models.MarketplaceModel.objects.filter(
                user=request.user
            ).order_by("-created_at")
            return render(
                request,
                "user-marketplace.html",
                {"navbarActive": "marketplace", "marketplace_items": marketplace_items},
            )
        return redirect("login")


class MarketplaceSearchView(View):
    def get(self, request):
        if request.user.is_authenticated:
            search = request.GET.get("search")
            marketplace_items = models.MarketplaceModel.objects.filter(
                title__icontains=search
            )
            categories = models.MarketplaceCategoryModel.objects.all()
            return render(
                request,
                "marketplace-user.html",
                {
                    "navbarActive": "marketplace",
                    "marketplace_items": marketplace_items,
                    "categories": categories,
                },
            )
        return redirect("login")


class MarketplaceCategoryView(View):
    def get(self, request):
        if request.user.is_authenticated:
            category = request.GET.get("category")
            marketplace_items = models.MarketplaceModel.objects.filter(
                category=category
            )
            categories = models.MarketplaceCategoryModel.objects.all()
            return render(
                request,
                "marketplace-user.html",
                {
                    "navbarActive": "marketplace",
                    "marketplace_items": marketplace_items,
                    "categories": categories,
                },
            )
        return redirect("login")


class UserMarketplaceEditView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            marketplace_item = models.MarketplaceModel.objects.get(pk=pk)
            marketplace_item_form = forms.MarketplaceForm(
                initial={
                    "category": marketplace_item.category,
                    "title": marketplace_item.title,
                    "description": marketplace_item.description,
                    "image": marketplace_item.image,
                    "image_2": marketplace_item.image_2,
                    "image_3": marketplace_item.image_3,
                    "image_4": marketplace_item.image_4,
                    "price": marketplace_item.price,
                    "contact": marketplace_item.contact,
                }
            )
            return render(
                request,
                "user-marketplace-edit.html",
                {
                    "navbarActive": "marketplace",
                    "marketplace_item_form": marketplace_item_form,
                },
            )
        return redirect("login")

    def post(self, request, pk):
        marketplace_item_form = forms.MarketplaceForm(request.POST, request.FILES)
        if marketplace_item_form.is_valid():
            category = marketplace_item_form.cleaned_data["category"]
            title = marketplace_item_form.cleaned_data["title"]
            description = marketplace_item_form.cleaned_data["description"]
            price = marketplace_item_form.cleaned_data["price"]
            image = marketplace_item_form.cleaned_data["image"]
            image_2 = marketplace_item_form.cleaned_data["image_2"]
            image_3 = marketplace_item_form.cleaned_data["image_3"]
            image_4 = marketplace_item_form.cleaned_data["image_4"]
            contact = marketplace_item_form.cleaned_data["contact"]
            marketplace_item = models.MarketplaceModel.objects.get(pk=pk)
            marketplace_item.category = category
            marketplace_item.title = title
            marketplace_item.description = description
            marketplace_item.price = price
            marketplace_item.image = image
            marketplace_item.image_2 = image_2
            marketplace_item.image_3 = image_3
            marketplace_item.image_4 = image_4
            marketplace_item.contact = contact
            marketplace_item.save()
            return redirect("user_marketplace")
        else:
            print(marketplace_item_form.errors)
            return render(
                request,
                "user-marketplace-edit.html",
                {
                    "navbarActive": "marketplace",
                    "marketplace_item_form": marketplace_item_form,
                    "error": marketplace_item_form.errors,
                },
            )


class UserMarketplaceDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            marketplace_item = models.MarketplaceModel.objects.get(pk=pk)
            marketplace_item.delete()
            return redirect("user_marketplace")
        return redirect("login")


class MarketplaceItemView(View):
    def get(self, request, pk):
        marketplace_item = models.MarketplaceModel.objects.get(pk=pk)
        similar_items = (
            models.MarketplaceModel.objects.filter(category=marketplace_item.category)
            .order_by("-created_at")
            .exclude(pk=pk)[:4]
        )
        return render(
            request,
            "marketplace-item.html",
            {
                "navbarActive": "marketplace",
                "marketplace_item": marketplace_item,
                "similar_items": similar_items,
            },
        )


class MarketplaceItemNewView(View):
    def get(self, request):
        if request.user.is_authenticated:
            marketplace_item_form = forms.MarketplaceForm()
            return render(
                request,
                "marketplace-item-new.html",
                {
                    "navbarActive": "marketplace",
                    "marketplace_item_form": marketplace_item_form,
                },
            )
        return redirect("login")

    def post(self, request):
        marketplace_item_form = forms.MarketplaceForm(request.POST, request.FILES)
        if marketplace_item_form.is_valid():
            category = marketplace_item_form.cleaned_data["category"]
            title = marketplace_item_form.cleaned_data["title"]
            description = marketplace_item_form.cleaned_data["description"]
            price = marketplace_item_form.cleaned_data["price"]
            image = marketplace_item_form.cleaned_data["image"]
            image_2 = marketplace_item_form.cleaned_data["image_2"]
            image_3 = marketplace_item_form.cleaned_data["image_3"]
            image_4 = marketplace_item_form.cleaned_data["image_4"]
            contact = marketplace_item_form.cleaned_data["contact"]
            user = request.user
            marketplace_item = models.MarketplaceModel(
                category=category,
                title=title,
                description=description,
                price=price,
                image=image,
                image_2=image_2,
                image_3=image_3,
                image_4=image_4,
                contact=contact,
                user=user,
            )
            marketplace_item.save()
            messages.success(request, "Item added successfully")
            return redirect("marketplace")
        else:
            print(marketplace_item_form.errors)
            return render(
                request,
                "marketplace-item-new.html",
                {
                    "navbarActive": "marketplace",
                    "marketplace_item_form": marketplace_item_form,
                    "error": marketplace_item_form.errors,
                },
            )


class RoomFinderView(View):
    def get(self, request):
        if request.user.is_authenticated:
            roomfinder_items = models.RoomFinderModel.objects.all().order_by(
                "-created_at"
            )
            return render(
                request,
                "roomfinder-user.html",
                {"navbarActive": "roomfinder", "roomfinder_items": roomfinder_items},
            )
        return render(request, "roomfinder.html", {"navbarActive": "roomfinder"})


class UserRoomFinderView(View):
    def get(self, request):
        if request.user.is_authenticated:
            roomfinder_items = models.RoomFinderModel.objects.filter(
                user=request.user
            ).order_by("-created_at")
            return render(
                request,
                "user-roomfinder.html",
                {"navbarActive": "roomfinder", "roomfinder_items": roomfinder_items},
            )
        return redirect("login")


class RoomFinderSearchView(View):
    def get(self, request):
        if request.user.is_authenticated:
            search = request.GET.get("search")
            roomfinder_items = models.RoomFinderModel.objects.filter(
                title__icontains=search
            )
            return render(
                request,
                "roomfinder-user.html",
                {
                    "navbarActive": "roomfinder",
                    "roomfinder_items": roomfinder_items,
                },
            )
        return redirect("login")


class UserRoomFinderEditView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            roomfinder_item = models.RoomFinderModel.objects.get(pk=pk)
            roomfinder_item_form = forms.RoomFinderForm(
                initial={
                    "title": roomfinder_item.title,
                    "description": roomfinder_item.description,
                    "location": roomfinder_item.location,
                    "no_of_availability": roomfinder_item.no_of_availability,
                    "image": roomfinder_item.image,
                    "image_2": roomfinder_item.image_2,
                    "image_3": roomfinder_item.image_3,
                    "image_4": roomfinder_item.image_4,
                    "contact": roomfinder_item.contact,
                    "available_from": roomfinder_item.available_from,
                    "room_type": roomfinder_item.room_type,
                    "prefered_gender": roomfinder_item.prefered_gender,
                    "stay_type": roomfinder_item.stay_type,
                    "smoking_preference": roomfinder_item.smoking_preference,
                    "vegetarian_preference": roomfinder_item.vegetarian_preference,
                    "pet_preference": roomfinder_item.pet_preference,
                    "alcohol_preference": roomfinder_item.alcohol_preference,
                }
            )
            return render(
                request,
                "user-roomfinder-edit.html",
                {
                    "navbarActive": "roomfinder",
                    "roomfinder_item_form": roomfinder_item_form,
                },
            )
        return redirect("login")

    def post(self, request, pk):
        roomfinder_item_form = forms.RoomFinderForm(request.POST)
        if roomfinder_item_form.is_valid():
            roomfinder_item = models.RoomFinderModel.objects.get(pk=pk)
            roomfinder_item.title = roomfinder_item_form.cleaned_data["title"]
            roomfinder_item.description = roomfinder_item_form.cleaned_data[
                "description"
            ]
            roomfinder_item.location
            roomfinder_item.no_of_availability = roomfinder_item_form.cleaned_data[
                "no_of_availability"
            ]
            roomfinder_item.image = roomfinder_item_form.cleaned_data["image"]
            roomfinder_item.image_2 = roomfinder_item_form.cleaned_data["image_2"]
            roomfinder_item.image_3 = roomfinder_item_form.cleaned_data["image_3"]
            roomfinder_item.image_4 = roomfinder_item_form.cleaned_data["image_4"]
            roomfinder_item.contact = roomfinder_item_form.cleaned_data["contact"]
            roomfinder_item.available_from = roomfinder_item_form.cleaned_data[
                "available_from"
            ]
            roomfinder_item.room_type = roomfinder_item_form.cleaned_data["room_type"]
            roomfinder_item.prefered_gender = roomfinder_item_form.cleaned_data[
                "prefered_gender"
            ]
            roomfinder_item.stay_type = roomfinder_item_form.cleaned_data["stay_type"]
            roomfinder_item.smoking_preference = roomfinder_item_form.cleaned_data[
                "smoking_preference"
            ]
            roomfinder_item.vegetarian_preference = roomfinder_item_form.cleaned_data[
                "vegetarian_preference"
            ]
            roomfinder_item.pet_preference = roomfinder_item_form.cleaned_data[
                "pet_preference"
            ]
            roomfinder_item.alcohol_preference = roomfinder_item_form.cleaned_data[
                "alcohol_preference"
            ]
            roomfinder_item.save()
            return redirect("user_roomfinder")
        else:
            print(roomfinder_item_form.errors)
            return render(
                request,
                "user-roomfinder-edit.html",
                {
                    "navbarActive": "roomfinder",
                    "roomfinder_item_form": roomfinder_item_form,
                    "error": roomfinder_item_form.errors,
                },
            )


class UserRoomFinderDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            roomfinder_item = models.RoomFinderModel.objects.get(pk=pk)
            roomfinder_item.delete()
            return redirect("user_roomfinder")
        return redirect("login")


class RoomFinderRoomView(View):
    def get(self, request, pk):
        roomfinder_item = models.RoomFinderModel.objects.get(pk=pk)
        similar_items = (
            models.RoomFinderModel.objects.all()
            .order_by("-created_at")
            .exclude(pk=pk)[:4]
        )
        return render(
            request,
            "roomfinder-room.html",
            {
                "navbarActive": "roomfinder",
                "roomfinder_item": roomfinder_item,
                "similar_items": similar_items,
            },
        )


class RoomFinderRoomNewView(View):

    def get(self, request):
        if request.user.is_authenticated:
            roomfinder_room_form = forms.RoomFinderForm()
            return render(
                request,
                "roomfinder-room-new.html",
                {
                    "navbarActive": "roomfinder",
                    "roomfinder_room_form": roomfinder_room_form,
                },
            )
        return redirect("login")

    def post(self, request):
        roomfinder_item_form = forms.RoomFinderForm(request.POST, request.FILES)
        if roomfinder_item_form.is_valid():
            title = roomfinder_item_form.cleaned_data["title"]
            description = roomfinder_item_form.cleaned_data["description"]
            location = roomfinder_item_form.cleaned_data["location"]
            no_of_availability = roomfinder_item_form.cleaned_data["no_of_availability"]
            image = roomfinder_item_form.cleaned_data["image"]
            image_2 = roomfinder_item_form.cleaned_data["image_2"]
            image_3 = roomfinder_item_form.cleaned_data["image_3"]
            image_4 = roomfinder_item_form.cleaned_data["image_4"]
            contact = roomfinder_item_form.cleaned_data["contact"]
            available_from = roomfinder_item_form.cleaned_data["available_from"]
            room_type = roomfinder_item_form.cleaned_data["room_type"]
            prefered_gender = roomfinder_item_form.cleaned_data["prefered_gender"]
            stay_type = roomfinder_item_form.cleaned_data["stay_type"]
            smoking_preference = roomfinder_item_form.cleaned_data["smoking_preference"]
            vegetarian_preference = roomfinder_item_form.cleaned_data[
                "vegetarian_preference"
            ]
            pet_preference = roomfinder_item_form.cleaned_data["pet_preference"]
            alcohol_preference = roomfinder_item_form.cleaned_data["alcohol_preference"]
            user = request.user
            roomfinder_item = models.RoomFinderModel(
                title=title,
                description=description,
                location=location,
                no_of_availability=no_of_availability,
                image=image,
                image_2=image_2,
                image_3=image_3,
                image_4=image_4,
                contact=contact,
                available_from=available_from,
                room_type=room_type,
                prefered_gender=prefered_gender,
                stay_type=stay_type,
                smoking_preference=smoking_preference,
                vegetarian_preference=vegetarian_preference,
                pet_preference=pet_preference,
                alcohol_preference=alcohol_preference,
                user=user,
            )
            roomfinder_item.save()
            messages.success(request, "Item added successfully")
            return redirect("roomfinder")
        else:
            print(roomfinder_item_form.errors)
            return render(
                request,
                "roomfinder-room-new.html",
                {
                    "navbarActive": "roomfinder",
                    "roomfinder_item_form": roomfinder_item_form,
                    "error": roomfinder_item_form.errors,
                },
            )


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


class UserRideShareView(View):
    def get(self, request):
        if request.user.is_authenticated:
            rideshare_items = models.RideShareModel.objects.filter(
                user=request.user
            ).order_by("-created_at")
            return render(
                request,
                "user-rideshare.html",
                {"navbarActive": "rideshare", "rideshare_items": rideshare_items},
            )
        return redirect("login")


class RideShareSearchView(View):
    def get(self, request):
        if request.user.is_authenticated:
            search = request.GET.get("search")
            rideshare_items = models.RideShareModel.objects.filter(
                start_location__icontains=search
            )
            return render(
                request,
                "rideshare-user.html",
                {
                    "navbarActive": "rideshare",
                    "rideshare_items": rideshare_items,
                },
            )
        return redirect("login")


class UserRideShareEditView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            rideshare_item = models.RideShareModel.objects.get(pk=pk)
            rideshare_item_form = forms.RideShareForm(
                initial={
                    "start_location": rideshare_item.start_location,
                    "end_location": rideshare_item.end_location,
                    "datetime": rideshare_item.datetime,
                    "description": rideshare_item.description,
                    "image": rideshare_item.image,
                    "image_2": rideshare_item.image_2,
                    "image_3": rideshare_item.image_3,
                    "image_4": rideshare_item.image_4,
                    "available_seats": rideshare_item.available_seats,
                    "total_seats": rideshare_item.total_seats,
                    "contact": rideshare_item.contact,
                }
            )
            return render(
                request,
                "user-rideshare-edit.html",
                {
                    "navbarActive": "rideshare",
                    "rideshare_item_form": rideshare_item_form,
                },
            )
        return redirect("login")

    def post(self, request, pk):
        rideshare_item_form = forms.RideShareForm(request.POST)
        if rideshare_item_form.is_valid():
            rideshare_item = models.RideShareModel.objects.get(pk=pk)
            rideshare_item.start_location = rideshare_item_form.cleaned_data[
                "start_location"
            ]
            rideshare_item.end_location = rideshare_item_form.cleaned_data[
                "end_location"
            ]
            rideshare_item.datetime = rideshare_item_form.cleaned_data["datetime"]
            rideshare_item.description = rideshare_item_form.cleaned_data["description"]
            rideshare_item.image = rideshare_item_form.cleaned_data["image"]
            rideshare_item.image_2 = rideshare_item_form.cleaned_data["image_2"]
            rideshare_item.image_3 = rideshare_item_form.cleaned_data["image_3"]
            rideshare_item.image_4 = rideshare_item_form.cleaned_data["image_4"]
            rideshare_item.available_seats = rideshare_item_form.cleaned_data[
                "available_seats"
            ]
            rideshare_item.total_seats = rideshare_item_form.cleaned_data["total_seats"]
            rideshare_item.contact = rideshare_item_form.cleaned_data["contact"]
            rideshare_item.save()
            return redirect("user_rideshare")
        else:
            print(rideshare_item_form.errors)
            return render(
                request,
                "user-rideshare-edit.html",
                {
                    "navbarActive": "rideshare",
                    "rideshare_item_form": rideshare_item_form,
                    "error": rideshare_item_form.errors,
                },
            )


class UserRideShareDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            rideshare_item = models.RideShareModel.objects.get(pk=pk)
            rideshare_item.delete()
            return redirect("user_rideshare")
        return redirect("login")


class RideShareRideView(View):
    def get(self, request, pk):
        rideshare_item = models.RideShareModel.objects.get(pk=pk)
        similar_items = (
            models.RideShareModel.objects.all()
            .order_by("-created_at")
            .exclude(pk=pk)[:4]
        )
        return render(
            request,
            "rideshare-ride.html",
            {
                "navbarActive": "rideshare",
                "rideshare_item": rideshare_item,
                "similar_items": similar_items,
            },
        )


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
        rideshare_item_form = forms.RideShareForm(request.POST, request.FILES)
        if rideshare_item_form.is_valid():
            start_location = rideshare_item_form.cleaned_data["start_location"]
            end_location = rideshare_item_form.cleaned_data["end_location"]
            datetime = rideshare_item_form.cleaned_data["datetime"]
            description = rideshare_item_form.cleaned_data["description"]
            image = rideshare_item_form.cleaned_data["image"]
            image_2 = rideshare_item_form.cleaned_data["image_2"]
            image_3 = rideshare_item_form.cleaned_data["image_3"]
            image_4 = rideshare_item_form.cleaned_data["image_4"]
            available_seats = rideshare_item_form.cleaned_data["available_seats"]
            total_seats = rideshare_item_form.cleaned_data["total_seats"]
            contact = rideshare_item_form.cleaned_data["contact"]
            user = request.user
            rideshare_item = models.RideShareModel(
                start_location=start_location,
                end_location=end_location,
                datetime=datetime,
                description=description,
                image=image,
                image_2=image_2,
                image_3=image_3,
                image_4=image_4,
                available_seats=available_seats,
                total_seats=total_seats,
                contact=contact,
                user=user,
            )
            rideshare_item.save()
            messages.success(request, "Item added successfully")
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


class LostFoundView(View):
    def get(self, request):
        if request.user.is_authenticated:
            lostfound_items = models.LostAndFoundModel.objects.all().order_by(
                "-created_at"
            )
            categories = models.LostAndFoundCategoryModel.objects.all()
            return render(
                request,
                "lostfound-user.html",
                {
                    "navbarActive": "lostfound",
                    "lostfound_items": lostfound_items,
                    "categories": categories,
                },
            )
        return render(request, "lostfound.html", {"navbarActive": "lostfound"})


class UserLostFoundView(View):
    def get(self, request):
        if request.user.is_authenticated:
            lostfound_items = models.LostAndFoundModel.objects.filter(
                user=request.user
            ).order_by("-created_at")
            return render(
                request,
                "user-lostfound.html",
                {"navbarActive": "lostfound", "lostfound_items": lostfound_items},
            )
        return redirect("login")


class LostFoundSearchView(View):
    def get(self, request):
        if request.user.is_authenticated:
            search = request.GET.get("search")
            lostfound_items = models.LostAndFoundModel.objects.filter(
                title__icontains=search
            )
            return render(
                request,
                "lostfound-user.html",
                {
                    "navbarActive": "lostfound",
                    "lostfound_items": lostfound_items,
                },
            )
        return redirect("login")


class LostFoundCategoryView(View):
    def get(self, request):
        if request.user.is_authenticated:
            category = request.GET.get("category")
            lostfound_items = models.LostAndFoundModel.objects.filter(category=category)
            return render(
                request,
                "lostfound-user.html",
                {
                    "navbarActive": "lostfound",
                    "lostfound_items": lostfound_items,
                },
            )
        return redirect("login")


class UserLostFoundEditView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            lostfound_item = models.LostAndFoundModel.objects.get(pk=pk)
            lostfound_item_form = forms.LostAndFoundForm(
                initial={
                    "category": lostfound_item.category,
                    "title": lostfound_item.title,
                    "description": lostfound_item.description,
                    "image": lostfound_item.image,
                    "image_2": lostfound_item.image_2,
                    "image_3": lostfound_item.image_3,
                    "image_4": lostfound_item.image_4,
                    "contact": lostfound_item.contact,
                }
            )
            return render(
                request,
                "user-lostfound-edit.html",
                {
                    "navbarActive": "lostfound",
                    "lostfound_item_form": lostfound_item_form,
                },
            )
        return redirect("login")

    def post(self, request, pk):
        lostfound_item_form = forms.LostAndFoundForm(request.POST, request.FILES)
        if lostfound_item_form.is_valid():
            category = lostfound_item_form.cleaned_data["category"]
            title = lostfound_item_form.cleaned_data["title"]
            description = lostfound_item_form.cleaned_data["description"]
            image = lostfound_item_form.cleaned_data["image"]
            image_2 = lostfound_item_form.cleaned_data["image_2"]
            image_3 = lostfound_item_form.cleaned_data["image_3"]
            image_4 = lostfound_item_form.cleaned_data["image_4"]
            contact = lostfound_item_form.cleaned_data["contact"]
            lostfound_item = models.LostAndFoundModel.objects.get(pk=pk)
            lostfound_item.category = category
            lostfound_item.title = title
            lostfound_item.description = description
            lostfound_item.image = image
            lostfound_item.image_2 = image_2
            lostfound_item.image_3 = image_3
            lostfound_item.image_4 = image_4
            lostfound_item.contact = contact
            lostfound_item.save()
            return redirect("user_lostfound")
        else:
            print(lostfound_item_form.errors)
            return render(
                request,
                "user-lostfound-edit.html",
                {
                    "navbarActive": "lostfound",
                    "lostfound_item_form": lostfound_item_form,
                    "error": lostfound_item_form.errors,
                },
            )


class UserLostFoundDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            lostfound_item = models.LostAndFoundModel.objects.get(pk=pk)
            lostfound_item.delete()
            return redirect("user_lostfound")
        return redirect("login")


class LostFoundItemView(View):
    def get(self, request, pk):
        lostfound_item = models.LostAndFoundModel.objects.get(pk=pk)
        recent_items = (
            models.LostAndFoundModel.objects.all()
            .exclude(pk=pk)
            .order_by("-created_at")[:4]
        )
        return render(
            request,
            "lostfound-item.html",
            {
                "navbarActive": "lostfound",
                "lostfound_item": lostfound_item,
                "recent_items": recent_items,
            },
        )


class LostFoundItemNewView(View):

    def get(self, request):
        if request.user.is_authenticated:
            lostfound_item_form = forms.LostAndFoundForm()
            return render(
                request,
                "lostfound-item-new.html",
                {
                    "navbarActive": "lostfound",
                    "lostfound_item_form": lostfound_item_form,
                },
            )
        return redirect("login")

    def post(self, request):
        lostfound_item_form = forms.LostAndFoundForm(request.POST, request.FILES)
        if lostfound_item_form.is_valid():
            category = lostfound_item_form.cleaned_data["category"]
            title = lostfound_item_form.cleaned_data["title"]
            description = lostfound_item_form.cleaned_data["description"]
            image = lostfound_item_form.cleaned_data["image"]
            image_2 = lostfound_item_form.cleaned_data["image_2"]
            image_3 = lostfound_item_form.cleaned_data["image_3"]
            image_4 = lostfound_item_form.cleaned_data["image_4"]
            contact = lostfound_item_form.cleaned_data["contact"]
            user = request.user
            lostfound_item = models.LostAndFoundModel(
                category=category,
                title=title,
                description=description,
                image=image,
                image_2=image_2,
                image_3=image_3,
                image_4=image_4,
                contact=contact,
                user=user,
            )
            lostfound_item.save()
            messages.success(request, "Item added successfully")
            return redirect("lostfound")
        else:
            print(lostfound_item_form.errors)
            return render(
                request,
                "lostfound-item-new.html",
                {
                    "navbarActive": "lostfound",
                    "lostfound_item_form": lostfound_item_form,
                    "error": lostfound_item_form.errors,
                },
            )


class AboutView(View):
    def get(self, request):
        return render(request, "about.html", {"navbarActive": "about"})


class ContactView(View):
    def get(self, request):
        contact_form = forms.ContactForm()
        return render(
            request,
            "contact.html",
            {"navbarActive": "contact", "contact_form": contact_form},
        )

    def post(self, request):
        contact_form = forms.ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data["name"]
            email = contact_form.cleaned_data["email"]
            subject = contact_form.cleaned_data["subject"]
            message = contact_form.cleaned_data["message"]
            contact = models.ContactModel(
                name=name, email=email, subject=subject, message=message
            )
            contact.save()
            contact_form = forms.ContactForm()
            return render(
                request,
                "contact.html",
                {
                    "navbarActive": "contact",
                    "success": True,
                    "contact_form": contact_form,
                },
            )
        else:
            print(contact_form.errors)
            return render(
                request,
                "contact.html",
                {
                    "navbarActive": "contact",
                    "contact_form": contact_form,
                    "error": contact_form.errors,
                },
            )
