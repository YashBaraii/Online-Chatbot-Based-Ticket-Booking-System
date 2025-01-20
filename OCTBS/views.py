from django.shortcuts import render

def home(rerquest):
    return render(rerquest, 'website/index.html')

def login(rerquest):
    return render(rerquest, 'registration/login.html')

def signup(rerquest):
    return render(rerquest, 'registration/signup.html')

def interactive_maps(rerquest):
    return render(rerquest, 'website/interactive_maps.html')

def blog(rerquest):
    return render(rerquest, 'website/blog.html')

def store(rerquest):
    return render(rerquest, 'website/online_store.html')

def events(rerquest):
    return render(rerquest, 'website/events.html')

def payments(rerquest):
    return render(rerquest, 'website/payment.html') 

def success(rerquest):
    return render(rerquest, 'website/success.html')