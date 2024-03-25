from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    # User registration
    path("register/", views.RegisterView.as_view(), name="register"),
    
    # User login
    path("login/", views.LoginView.as_view(), name="login"),
    
    # User logout (requires login)
    path("logout/", login_required(views.LogoutView), name="logout"),
    
    # Home page
    path("", views.HomeView.as_view(), name="home"),

    # RideShare main page
    path("rideshare/", views.RideShareView.as_view(), name="rideshare"),
    
    # Specific RideShare ride page (requires login)
    path(
        "rideshare/ride/<int:pk>/",
        login_required(views.RideShareRideView.as_view()),
        name="rideshare_ride",
    ),
    
    # Create a new RideShare ride page (requires login)
    path(
        "rideshare/ride/new/",
        login_required(views.RideShareRideNewView.as_view()),
        name="rideshare_ride_new",
    ),

    # roomfinder pages
    path("roomfinder/", views.RoomFinderView.as_view(), name="roomfinder"),
    path(
        "roomfinder/room/<int:pk>/",
        login_required(views.RoomFinderRoomView.as_view()),
        name="roomfinder_room",
    ),
    path(
        "roomfinder/room/new/",
        login_required(views.RoomFinderRoomNewView.as_view()),
        name="roomfinder_room_new",
    ),
]
