from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q
from .models import Image, CustomUser, Favourite

def home(request):
    filter_type = request.GET.get("filter", "all")
    sort_type = request.GET.get("sortFilter", "date-desc")
    search_query = request.GET.get("search", "").strip()

    image_qs = Image.objects.all()
    if filter_type == "free":
        image_qs = image_qs.filter(is_paid=False)
    elif filter_type == "paid":
        image_qs = image_qs.filter(is_paid=True)

    if search_query:
        image_qs = image_qs.filter(
            Q(image_title__icontains=search_query) |
            Q(category__icontains=search_query) 
        )

    if sort_type == "price-asc":
        image_qs = image_qs.order_by("image_price")
    elif sort_type == "price-desc":
        image_qs = image_qs.order_by("-image_price")
    elif sort_type == "date-asc":
        image_qs = image_qs.order_by("created_at")
    else:  
        image_qs = image_qs.order_by("-created_at")

    images = image_qs

    favorite_image_ids = []
    if request.user.is_authenticated:
        favorite_image_ids = list(
            Favourite.objects.filter(user=request.user).values_list("image_id", flat=True)
        )
    return render(request, "home.html", {
        "images": images,
        "favorite_image_ids": favorite_image_ids,
        "active_filter": filter_type,
        "active_sort": sort_type,
        "search_query": search_query
    })


def image_detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favourite.objects.filter(user=request.user, image=image).exists()
    return render(request, "image-detail.html", {
        "image": image,
        "is_favorite": is_favorite
    })


def explore(request):
    return render(request, 'explore.html')

def about(request):
    return render(request, 'about.html')

def privacy(request):
    return render(request, 'PrivacyPolicy.html')

def terms_and_conditions(request):
    return render(request, 'Terms&Conditions.html')

@login_required
def favourites(request):
    # Get the actual Image objects that the user has favorited
    user_favorites = Image.objects.filter(favourite_entries__user=request.user)
    print(f"User {request.user.username} has {user_favorites.count()} favorites")
    for fav in user_favorites:
        print(f"  - {fav.image_title}")
    return render(request, 'favourites.html', {'favorites': user_favorites})

def toggle_favorite(request):
    print(f"Toggle favorite request: {request.method}, User: {request.user}, Authenticated: {request.user.is_authenticated}")
    
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Login required'}, status=401)
    
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        print(f"Image ID received: {image_id}")
        if not image_id:
            return JsonResponse({'error': 'Image ID required'}, status=400)
        
        try:
            image = Image.objects.get(id=image_id)
            print(f"Found image: {image.image_title}")
            
            favorite, created = Favourite.objects.get_or_create(
                user=request.user,
                image=image
            )
            print(f"Favorite created: {created}, Favorite ID: {favorite.id}")
            
            if created:
                print(f"Favorite created for user {request.user.username} and image {image_id}")
                return JsonResponse({
                    'success': True, 
                    'action': 'added',
                    'message': 'Added to favorites'
                })
            else:
                print(f"Favorite removed for user {request.user.username} and image {image_id}")
                favorite.delete()
                return JsonResponse({
                    'success': True, 
                    'action': 'removed',
                    'message': 'Removed from favorites'
                })
        except Image.DoesNotExist:
            return JsonResponse({'error': 'Image not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email and password:
            # Try to find user by email
            try:
                user = CustomUser.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Welcome back, {user.first_name}!')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid email or password.')
            except CustomUser.DoesNotExist:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'login.html')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        
        # Validation
        if not all([full_name, email, password, confirm_password]):
            messages.error(request, 'Please fill in all fields.')
        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'A user with this email already exists.')
        else:
            try:
                # Split full name into first and last name
                name_parts = full_name.split(' ', 1)
                first_name = name_parts[0]
                last_name = name_parts[1] if len(name_parts) > 1 else ''
                
                # Create username from email (before @)
                username = email.split('@')[0]
                
                # Ensure username is unique
                original_username = username
                counter = 1
                while CustomUser.objects.filter(username=username).exists():
                    username = f"{original_username}{counter}"
                    counter += 1
                
                # Create user
                user = CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                
                # Auto-login after registration
                login(request, user)
                messages.success(request, f'Account created successfully! Welcome, {user.first_name}!')
                return redirect('home')
                
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
    
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')

def travel(request):
    return render(request, "travel.html")

def profile(request):
    user = request.user
    context = {
        "name": f"{user.first_name} {user.last_name}",
        "email": user.email,
    }
    return render(request, "Profile.html", context)

def payment_success(request):
    return render(request, 'payment_success.html')

def payment_failure(request):
    return render(request, 'payment_failure.html')




