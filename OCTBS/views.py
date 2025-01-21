from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import logout
from django.http import HttpResponse

def home(request):
    return render(request, 'website/index.html')

@login_required
def interactive_maps(request):
    return render(request, 'website/interactive_maps.html')

@login_required
def blog(request):
    return render(request, 'website/blog.html')

@login_required
def store(request):
    return render(request, 'website/online_store.html')

@login_required
def events(request):
    return render(request, 'website/events.html')

@login_required
def payments(request):
    return render(request, 'website/payment.html')

@login_required
def success(request):
    return render(request, 'website/success.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

