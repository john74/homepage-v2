from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from users.models import User


def home(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('authentication/login/')

    context = {}
    return render(request, 'home.html', context)
