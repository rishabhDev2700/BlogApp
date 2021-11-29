from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

# Create your views here.
from Authentication.form import UserUpdateForm, UserRegistrationForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'auth/login.html', )


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form': form})
