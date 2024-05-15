from django.contrib.auth.models import User
from . import models

# Custom context processor to provide user data to templates
def user_data(request):
    # Get the current user from the request
    user = request.user
    # Check if the user is authenticated
    if user.is_authenticated:
        # If authenticated, retrieve the user data from the database
        user_data = User.objects.get(username=user.username)
        return {"user_data": user_data}
    else:
        # If not authenticated, provide default guest user data
        return {
            "user_data": {
                "username": "guest",
                "first_name": "Guest",
                "last_name": "Guest",
                "email": "guest@guest.com",
            }
        }
