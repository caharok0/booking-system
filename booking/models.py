from django.db import models

# Create your models here.
class HouseModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="House Name")
    info = models.TextField(verbose_name="House Info")
    country = models.CharField(max_length=100, verbose_name="Country")
    address = models.CharField(max_length=100, verbose_name="Address")
    room_count = models.IntegerField(verbose_name="Room Count")
    people_count = models.IntegerField(verbose_name="People Count")
    square = models.IntegerField(verbose_name="Square")
    price_by_day = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price by Day")


    is_booked = models.BooleanField(default=False, verbose_name="Is Booked")

    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.name} - {self.country} - {self.address} - {self.room_count} - {self.people_count} - {self.square} - {self.price_by_day} - {self.is_booked}"


    class Meta:
        verbose_name = "House"
        verbose_name_plural = "Houses"
        ordering = ["-created_at"]
    
class BookingModel(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    house = models.ForeignKey(HouseModel, on_delete=models.CASCADE, verbose_name="House")
    arrival_date = models.DateField(verbose_name="Arrival Date")
    departure_date = models.DateField(verbose_name="Departure Date")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="Status")
    comments = models.TextField(blank=True, verbose_name="Comments")


    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.house.name} - {self.arrival_date} - {self.departure_date} - {self.status} - {self.comments}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["-created_at"]

    