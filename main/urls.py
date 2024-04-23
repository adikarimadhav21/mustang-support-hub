from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    # Authentication URLs
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", login_required(views.LogoutView), name="logout"),
    path("password-reset/", views.PasswordResetView.as_view(), name="password_reset"),
    
    # Profile URLs
    path("profile/edit", login_required(views.ProfileEditView.as_view()), name="profile_edit"),
    
    # User Marketplace URLs
    path("user/marketplace/", login_required(views.UserMarketplaceView.as_view()), name="user_marketplace"),
    path("user/marketplace/edit/<int:pk>/", login_required(views.UserMarketplaceEditView.as_view()), name="user_marketplace_edit"),
    path("user/marketplace/delete/<int:pk>/", login_required(views.UserMarketplaceDeleteView.as_view()), name="user_marketplace_delete"),
    
    # User Room Finder URLs
    path("user/roomfinder/", login_required(views.UserRoomFinderView.as_view()), name="user_roomfinder"),
    path("user/roomfinder/edit/<int:pk>/", login_required(views.UserRoomFinderEditView.as_view()), name="user_roomfinder_edit"),
    path("user/roomfinder/delete/<int:pk>/", login_required(views.UserRoomFinderDeleteView.as_view()), name="user_roomfinder_delete"),
    
    # User Ride Share URLs
    path("user/rideshare/", login_required(views.UserRideShareView.as_view()), name="user_rideshare"),
    path("user/rideshare/edit/<int:pk>/", login_required(views.UserRideShareEditView.as_view()), name="user_rideshare_edit"),
    path("user/rideshare/delete/<int:pk>/", login_required(views.UserRideShareDeleteView.as_view()), name="user_rideshare_delete"),
    
    # User Lost and Found URLs
    path("user/lostfound/", login_required(views.UserLostFoundView.as_view()), name="user_lostfound"),
    path("user/lostfound/edit/<int:pk>/", login_required(views.UserLostFoundEditView.as_view()), name="user_lostfound_edit"),
    path("user/lostfound/delete/<int:pk>/", login_required(views.UserLostFoundDeleteView.as_view()), name="user_lostfound_delete"),
    
    # Home URL
    path("", views.HomeView.as_view(), name="home"),
    
    # Marketplace URLs
    path("marketplace/", views.MarketplaceView.as_view(), name="marketplace"),
    path("marketplace/search/", login_required(views.MarketplaceSearchView.as_view()), name="marketplace_search"),
    path("marketplace/category/", login_required(views.MarketplaceCategoryView.as_view()), name="marketplace_category"),
    path("marketplace/item/<int:pk>/", login_required(views.MarketplaceItemView.as_view()), name="marketplace_item"),
    path("marketplace/item/new/", login_required(views.MarketplaceItemNewView.as_view()), name="marketplace_item_new"),
    
    # Room Finder URLs
    path("roomfinder/", views.RoomFinderView.as_view(), name="roomfinder"),
    path("roomfinder/search/", login_required(views.RoomFinderSearchView.as_view()), name="roomfinder_search"),
    path("roomfinder/room/<int:pk>/", login_required(views.RoomFinderRoomView.as_view()), name="roomfinder_room"),
    path("roomfinder/room/new/", login_required(views.RoomFinderRoomNewView.as_view()), name="roomfinder_room_new"),
    
    # Ride Share URLs
    path("rideshare/", views.RideShareView.as_view(), name="rideshare"),
    path("rideshare/search/", login_required(views.RideShareSearchView.as_view()), name="rideshare_search"),
    path("rideshare/ride/<int:pk>/", login_required(views.RideShareRideView.as_view()), name="rideshare_ride"),
    path("rideshare/ride/new/", login_required(views.RideShareRideNewView.as_view()), name="rideshare_ride_new"),
    
    # Lost and Found URLs
    path("lostfound/", views.LostFoundView.as_view(), name="lostfound"),
    path("lostfound/search/", login_required(views.LostFoundSearchView.as_view()), name="lostfound_search"),
    path("lostfound/category/", login_required(views.LostFoundCategoryView.as_view()), name="lostfound_category"),
    path("lostfound/item/<int:pk>/", login_required(views.LostFoundItemView.as_view()), name="lostfound_item"),
    path("lostfound/item/new/", login_required(views.LostFoundItemNewView.as_view()), name="lostfound_item_new"),
    
    # About and Contact URLs
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]
