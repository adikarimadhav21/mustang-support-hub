from django.urls import path
from django.contrib.auth.decorators import login_required


from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", login_required(views.LogoutView), name="logout"),
    #
    path("", views.HomeView.as_view(), name="home"),
    
]
