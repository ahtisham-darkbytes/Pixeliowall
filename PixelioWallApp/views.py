from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def explore(request):
    return render(request, 'explore.html')

def about(request):
    return render(request, 'about.html')

def privacy(request):
    return render(request, 'PrivacyPolicy.html')

def favourites(request):
    return render(request, 'favourites.html')

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def travel(request):
    return render(request, "travel.html")

def profile(request):
    return render(request, "Profile.html")

def payment_success(request):
    return render(request, 'payment_success.html')

def payment_failure(request):
    return render(request, 'payment_failure.html')

def image_detail(request):
    return render(request, "image-detail.html")

