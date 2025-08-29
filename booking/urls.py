from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import register, login_check, home, logout_view

urlpatterns = [
    # path('rsave',rsave,name="rsave"),
    # path('login_check',login_check,name="login_check"),
    # path('register/', register, name='register'),
    # path('', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
    # path('home/', home, name='home'),


    path("", login_check, name="login"),
    path("register/", register, name="register"),
    path("login_check/", login_check, name="login_check"),
    path("home/", home, name="home"),
    path("logout/", logout_view, name="logout"),
    path('create/', create_travel_option, name='create_travel_option'),
    path('list/', list_travel_options, name='list_travel_options'),
   # path('book/', book_travel_option, name='book_travel_option'),
    path('book/', book_travel, name='book_travel'),
    path('success/', booking_success, name='booking_success'),
    path('my-bookings/', my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', cancel_booking, name='cancel_booking'),
    path('update-profile/', update_profile, name='update_profile'),
]