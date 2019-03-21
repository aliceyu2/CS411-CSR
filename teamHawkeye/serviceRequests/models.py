from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from localflavor.us.us_states import STATE_CHOICES


class Request(models.Model):
    REQUEST_TYPES = (
        ('P', 'Pot Hole Request'),
        ('A', 'Abandoned Vehicle Request'),
    )
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    requestNumber = models.PositiveIntegerField(primary_key = True, default = 1)
    creationDate = models.DateTimeField(default = timezone.now)
    completionDate = models.DateTimeField(null = True, blank = True)
    requestType = models.CharField(choices = REQUEST_TYPES, default = "P", max_length = 255)
    status = models.CharField(max_length = 100, default = "In Progress")
    priority = models.IntegerField(default = 1)
    address = models.CharField(max_length = 255, default = "500 W Madison St")
    city = models.CharField(max_length = 255, default = "Chicago")
    state = models.CharField(choices = STATE_CHOICES, default = "Illinois", max_length = 255)
    zipCode = models.IntegerField(default = 60661)

    def save(self, *args, **kwargs):
        super().save()