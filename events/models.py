from django.db import models
from django.utils import timezone
from notification.models import Notifications,Groups
from account.models import CustomUser

# Create your models here.
class Event(models.Model):

    name = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    duration = models.CharField(max_length = 100)
    type = models.IntegerField(choices = ((1,'Virtual'),(2,'Physical')))
    veneu = models.CharField(max_length = 200) #platform
    url_location = models.CharField(max_length = 2000,null=True)
    description = models.CharField(max_length = 2000,default = '')
    guest_description = models.CharField(max_length = 2000,default = '')
    ticket_pricing_description = models.CharField(max_length = 2000,default = 'event info')
    banner = models.ImageField(upload_to='event/banner',null = True)
    created_date = models.DateTimeField(auto_now_add = True)

    groups = models.ManyToManyField(Groups,related_name = "events")
    status = models.BooleanField(default = True)

    FREE = 'free'
    PAID = 'paid'
    PRICING_CHOICES = [
        (FREE, 'Free'),
        (PAID, 'Paid'),
    ]
    pricing_type = models.CharField(max_length=10, choices=PRICING_CHOICES, default=FREE)
    pricing_description = models.CharField(max_length=2000, default='', blank=True, null=True)

    


    def is_free_event(self):
        return self.pricing_type == self.FREE

    def is_paid_event(self):
        return self.pricing_type == self.PAID



    
    def __str__(self):
        return self.name

    
class TicketType(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ticket_types')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, default='', blank=True)
    limit = models.PositiveIntegerField(default=0)  # 0 for unlimited
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.event.name} - {self.name}"
    

class Participation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participations', null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)  # For non-registered users
    email = models.EmailField(blank=True)  # For non-registered users
    phone_number = models.CharField(max_length=15, blank=True)
    not_interested = models.BooleanField(default=False) 
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.SET_NULL, null=True, blank=True)
    payment_screenshot = models.ImageField(upload_to='event/payment_screenshots/', blank=True, null=True)

    def __str__(self):
        return f"{self.name}-{self.event}"

    class Meta:
        # Enforcing unique participation per user and event
        unique_together = ['event', 'user']

