from django.db import models

class Booking(models.Model):
    EventChoice = [
        ('pre/Post-Wedding', 'pre/Post-Wedding'),
        ('Wedding', 'Wedding'),
        ('Birthday', 'Birthday'),
        ('Engagement', 'Engagement'),
        ('Anniversary', 'Anniversary'),
        ('baby-Shower', 'baby-Shower'),
        ('Maternity', 'Maternity'),
        ('maternity', 'maternity'),
        ('Corporate-Event', 'Corporate-Event'),
        ('Others', 'Others'),
    ]

    Fname = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100, unique=True, null=True)
    Phone = models.CharField(max_length=12,blank=True, null=True, unique=True)
    AlterNumber = models.CharField(max_length=12,blank=True, null=True, unique=True)
    Address = models.TextField(max_length=200)
    EventType= models.CharField(max_length=100, choices=EventChoice)
    Date = models.DateField()
    Time = models.TimeField()
    Message = models.TextField(max_length=200 , blank=True, null=True)

    class Meta:
        db_table = 'studio_booking'   

    def __str__(self):
        return f"""{self.Fname} {self.Email} {self.Phone} {self.AlterNumber} {self.Address}  {self.EventType}
          {self.Date} {self.Time} {self.Message}"""

class Rentequipment(models.Model):
    EquipmentChoice = [
        ('Drone Single', 'Drone'),
        ('LED Wall', 'LED Wall'),
        ('LED Plasma', 'LED Plasma'),
        ('Crane', 'Crane'),
        ('Flower Drone', 'Flower Drone'),
        ('varmala Drone', 'varmala Drone'),
    ]

    CName = models.CharField(max_length=100)
    CEmail = models.EmailField(max_length=100, unique=True, null=True)
    CNumber = models.CharField(max_length=12,blank=True, null=True, unique=True)
    CAddress = models.TextField(max_length=200)
    EquipmentType = models.CharField(max_length=100, choices=EquipmentChoice)
    EquipmentQuantity = models.IntegerField()
    # EquipmentPrice = models.FloatField()
    EquipmentDescription = models.TextField(max_length=200 , blank=True, null=True)

    class Meta:
        db_table = 'rent_equipment'   

    def __str__(self):
        return f"""{self.CName} {self.CEmail} {self.CNumber} {self.CAddress}
         {self.EquipmentType} {self.EquipmentQuantity} {self.EquipmentDescription}"""
















# Create your models here.

# event_type = models.CharField(max_length=10, choices=EventChoice)
    # event_name = models.CharField(max_length=100)
    # event_date = models.DateField()
    # event_time = models.TimeField()
    # event_location = models.CharField(max_length=100)
    # event_address = models.TextField()
    # event_message = models.TextField()
    # event_email = models.EmailField()
    # event_phone = models.CharField(max_length=12)
    # event_guests = models.IntegerField()
    # event_budget = models.FloatField()
    # event_status = models.CharField(max_length=10, choices=BookingStatusChoice, default='Pending' 
    # event_created_at = models.DateTimeField(auto_now_add=True)
    # event_updated_at = models.DateTimeField(auto_now=True)
    # event_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # event_updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # event_deleted = models.BooleanField(default=False)
    # event_deleted_at = models.DateTimeField(null=True)
    # event_deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # event_deleted_reason = models.TextField(null=True)
    # event_deleted_remark = models.TextField(null=True)
    # event_deleted_status = models.CharField(max_length=10, choices=BookingStatusChoice, null=True)
    # event_deleted_updated_at = models.DateTimeField(null=True)
    # event_deleted_updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # event_deleted_deleted = models.BooleanField(default=False)
    # event_deleted_deleted_at = models.DateTimeField(null=True)
    # event_deleted_deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # event_deleted_deleted_reason = models.TextField(null=True)