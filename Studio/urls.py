from django.urls import path
from. import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Plans', views.Plans, name='Plans'),
    path('Booking', views.Booking, name='Booking'),
    # path('Booking Success', views.BookingSuccess, name='Booking Success'),
]
