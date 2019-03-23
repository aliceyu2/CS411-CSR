from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from localflavor.us.us_states import STATE_CHOICES
from django.urls import reverse
from django.db import transaction


class Request(models.Model):
    REQUEST_TYPES = (
        ('P', 'Pot Hole Request'),
        ('A', 'Abandoned Vehicle Request'),
    )
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    requestNumber = models.IntegerField(primary_key = True)
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
        if self.pk is None:
            with transaction.atomic():
                oldReqNum = Request.objects.select_for_update(nowait=True).order_by('-requestNumber')[0]
                self.requestNumber = oldReqNum.requestNumber + 1
                super(Request, self).save(self, *args, **kwargs)
        else:
            super().save()
    
    def get_absolute_url(self):
        return reverse('srDetail', kwargs={'pk': self.pk})