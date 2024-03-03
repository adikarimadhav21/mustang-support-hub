from django.shortcuts import redirect, render
from django.http import HttpResponseNotFound
from django.views import View

from . import models


# homepage view
class home(View):

    def get(self, request):
        return render(request, "index.html")
