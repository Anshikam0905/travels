from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class login(models.Model):
    email = models.CharField(unique=True,max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.email

#register

class Register(models.Model):
    #id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=8)
    def __str__(self):
        return self.email
    

class TravelOption(models.Model):
    TRAVEL_TYPE_CHOICES = [
        ('Flight', 'Flight'),
        ('Train', 'Train'),
        ('Bus', 'Bus'),
    ]

    travel_id = models.AutoField(primary_key=True)
    travel_type = models.CharField(max_length=10, choices=TRAVEL_TYPE_CHOICES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.travel_type} from {self.source} to {self.destination} on {self.date_time.strftime('%Y-%m-%d %H:%M')}"



# class Booking(models.Model):
#     travel_otion = models.ForignKey(TravelOption, on_delete=models.CASCADE)
#     name = models.CharFild(max_length=100)
#     seats_boked = models.PositiveIntegerField()
#     booking_ime = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name} - {self.travel_option} - {self.seats_booked} seat(s)"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    number_of_seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Confirmed')
    source = models.CharField(max_length=100, default="")
    destination = models.CharField(max_length=100, default="")



    def save(self, *args, **kwargs):
        self.total_price = self.number_of_seats * self.travel_option.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.travel_option} - {self.status}"

