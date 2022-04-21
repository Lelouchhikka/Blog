from django.shortcuts import render, redirect
from auth_user.forms import UserForm, ProfileForm
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/news')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/news')
            else:
                return render(request, 'auth/login.html', {
                    'error': 'Email or Password error'
                })
        else:
            return render(request, 'auth/login.html')

def signup_user(request):
    if request.user.is_authenticated:
        return redirect('/news')
    else:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                UserProfile.objects.create(user=user, iin=request.POST.get('iin'), phone=request.POST.get('phone'))
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('/news')
            else:
                profile = ProfileForm()
                return render(request, 'auth/signup.html', {
                'form': form,
                'error': 'Email or Password error',
                'profile': profile
            })
        else:
            form = UserForm()
            profile = ProfileForm()
            return render(request, 'auth/signup.html', {
                'form': form,
                'profile': profile
            })

def logout_user(request):
    logout(request)
    return redirect('login')

