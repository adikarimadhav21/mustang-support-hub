from django.urls import path

from . import views

urlpatterns = [
    # homepage
    path("", views.home.as_view(), name="home"),
]
