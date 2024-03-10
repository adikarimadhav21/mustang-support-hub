from django.urls import path
from django.contrib.auth.decorators import login_required


from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    #
    path("", views.HomeView.as_view(), name="home"),
    
]
