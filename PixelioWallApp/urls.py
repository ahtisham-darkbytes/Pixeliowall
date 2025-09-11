from django.urls import path
from PixelioWallApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('favourites/', views.favourites, name='favourites'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path("travel/", views.travel, name="travel"), 
    path("profile/", views.profile, name="profile"),
    path('payment-success/', views.payment_success, name='payment_success'), 
    path('payment-failure/', views.payment_failure, name='payment_failure'),
    path("image-detail/<uuid:image_id>/", views.image_detail, name="image-detail"),
    path('toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),

]
