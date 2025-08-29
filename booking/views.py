from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, UpdateProfileForm, TravelOptionForm, BookingForm
from .models import TravelOption, Booking
from django.http import HttpResponse

User = get_user_model()


# Register
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse("save")
            return redirect("login")
    else:
        form = RegisterForm()
        #return HttpResponse("not save")
    return render(request, "register.html", {"form": form})


# Login
def login_check(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid Email or Password"})

    return render(request, "login.html")


# Logout
def logout_view(request):
    logout(request)
    return redirect("login")


# Home Page
@login_required
def home(request):
    context = {
        "uname": request.user.first_name,
        "email": request.user.email,
    }
    return render(request, "home.html", context)


# Create Travel Option
@login_required
def create_travel_option(request):
    if request.method == "POST":
        form = TravelOptionForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse("save")
            return redirect("list_travel_options")
    else:
        form = TravelOptionForm()
    return render(request, "create_option.html", {"form": form})


# List Travel Options
def list_travel_options(request):
    options = TravelOption.objects.all()
    return render(request, "list_options.html", {"options": options})


# Book Travel
@login_required
def book_travel(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            travel = booking.travel_option

            if booking.number_of_seats <= travel.available_seats:
                booking.user = request.user
                travel.available_seats -= booking.number_of_seats
                travel.save()
                booking.save()
                #return HttpResponse("Sucess")
                return redirect("booking_success")
            else:
                form.add_error("number_of_seats", "Not enough seats available.")
    else:
        form = BookingForm()
    return render(request, "book_travel.html", {"form": form})


# Booking Success
def booking_success(request):
    return render(request, "success.html")


# Show My Bookings
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by("-booking_date")
    return render(request, "my_bookings.html", {"bookings": bookings})


# Cancel Booking
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if booking.status != "Cancelled":
        booking.status = "Cancelled"
        booking.travel_option.available_seats += booking.number_of_seats
        booking.travel_option.save()
        booking.save()

    return redirect("my_bookings")


# Update Profile
@login_required
def update_profile(request):
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, "update_profile.html", {"form": form})
