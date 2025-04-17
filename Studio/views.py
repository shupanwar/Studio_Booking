from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# from .models import Booking
from .forms import EventForm


def Home(self):
    return render(self, 'index.html')

def Booking(self):
    return render(self, 'booking.html')

def Plans(self):
    return render(self, 'plans.html')

def Booking(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been confirmed!')
            return HttpResponse('Thankyou for booking')
        else:
            messages.error(request, 'Please correct the error below.') 
    else:
        form = EventForm()

    return render(request, 'index.html', {'form': form})
