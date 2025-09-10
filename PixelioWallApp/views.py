from django.shortcuts import render, get_object_or_404
from .models import Image

def home(request):
    images = Image.objects.all().order_by("-created_at")
    return render(request, "home.html", {"images": images})


def image_detail(request):
    image_id = request.GET.get("id")
    image = get_object_or_404(Image, id=image_id)
    return render(request, "image-detail.html", {"image": image})


def explore(request):
    return render(request, 'explore.html')

def about(request):
    return render(request, 'about.html')

def privacy(request):
    return render(request, 'PrivacyPolicy.html')

def terms_and_conditions(request):
    return render(request, 'Terms&Conditions.html')

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



