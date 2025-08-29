from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Booking

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

from django import forms
from .models import TravelOption

class TravelOptionForm(forms.ModelForm):
    class Meta:
        model = TravelOption
        fields = '__all__'
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['travel_option', 'name', 'seats_booked']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['travel_option', 'source','destination','number_of_seats']

from django import forms
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

