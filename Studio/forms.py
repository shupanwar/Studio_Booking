from django import forms
from .models import Booking, Rentequipment

class EventForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'Fname',
            'Email', 
            'Phone', 
            'AlterNumber', 
            'Address', 
            'EventType', 
            'Date', 
            'Time', 
            'Message'
        ]
class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Rentequipment
        fields = [
            'CName',
            'CEmail', 
            'CNumber', 
            'CAddress', 
            'EquipmentType', 
            'EquipmentQuantity', 
            'EquipmentDescription'
        ]