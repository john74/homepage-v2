from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


def login_user(request):
    form = AuthenticationForm()
    if request.method != 'POST':
        context = {'form':form}
        return render(request, 'login.html', context)

    # the name attribute of AuthenticationForm is username
    email = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, email=email, password=password)
    if user:
        login(request, user)
    return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('login')