from django.db import models
from django.utils import timezone
from notification.models import Notifications,Groups


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
    ticket_pricing_description = models.CharField(max_length = 2000,default = '')
    banner = models.ImageField(upload_to='event/banner',null = True)
    created_date = models.DateTimeField(auto_now_add = True)

    groups = models.ManyToManyField(Groups,related_name = "events")
    status = models.BooleanField(default = True)

