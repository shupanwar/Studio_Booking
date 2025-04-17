from django.contrib import admin
from .models import Booking
from .forms import EventForm

admin.site.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('Booking-Fname',  'Booking-Email', 'Booking-Number', 'Booking-Alter-Number',
                'Booking-Address', 'Booking-Event', 'Booking-Date', 'Booking-Time', 
                'Booking-Message')
    search_fields = ('Booking-Fname','Booking-Email', 'Booking-Number', 'Booking-Alter-Number',
                    'Booking-Event')
    list_display = ('Booking-Fname', 'Booking-Email', 'Booking-Number', 'Booking-Alter-Number',
                    'Booking-Event')

# Register your models here.
