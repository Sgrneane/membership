from collections.abc import Iterable
from django.db import models
from account.models import CustomUser
from django.utils import timezone
# Create your models here.
class Groups(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 2000)
    users = models.ManyToManyField(CustomUser,related_name='notification_groups')
    created_at= models.DateTimeField(auto_now_add=True,null=True)

class Notifications(models.Model):
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    subject = models.CharField(max_length = 100)
    description = models.CharField(max_length = 2000)
    groups = models.ManyToManyField(Groups,related_name='groups')
    status = models.BooleanField()

    def __str__(self) -> str:
        return self.subject
