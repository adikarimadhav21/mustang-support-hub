from django.contrib.auth.models import User
from . import models


def user_data(request):
    user = request.user
    if user.is_authenticated:
        user_data = User.objects.get(username=user.username)
        return {"user_data": user_data}
    return {
        "user_data": {
            "username": "guest",
            "first_name": "Guest",
            "last_name": "Guest",
            "email": "Guest@guest.com",
        }
    }
