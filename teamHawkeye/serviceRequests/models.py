from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from localflavor.us.us_states import STATE_CHOICES
from django.urls import reverse
from django.db import transaction
from geopy.geocoders import Nominatim
from django.core.exceptions import ValidationError
from serviceRequests.AlertThread import distanceCheck
from threading import Thread
from django.db import connection

cursor = connection.cursor()


class Request(models.Model):
    REQUEST_TYPES = (
        ('PH', 'Pot Hole Request'),
        ('AV', 'Abandoned Vehicle Request'),
    )
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    requestNumber = models.AutoField(primary_key = True)
    creationDate = models.DateTimeField(default = timezone.now)
    completionDate = models.DateTimeField(null = True, blank = True)
    requestType = models.CharField(choices = REQUEST_TYPES, default = 'PH', max_length = 255)
    status = models.CharField(max_length = 100, default = "In Progress")
    priority = models.IntegerField(default = 1)
    address = models.CharField(max_length = 255, default = "500 W Madison St")
    city = models.CharField(max_length = 255, default = "Chicago")
    state = models.CharField(choices = STATE_CHOICES, default = "Illinois", max_length = 255)
    zipCode = models.IntegerField(default = 60661)
    cursor.execute('''CREATE OR REPLACE VIEW priorityView AS SELECT * FROM serviceRequests_request ORDER BY priority DESC''')
    # SHOW TABLES;
    cursor.close()

    def save(self, *args, **kwargs):
        if self.pk is None:
            with transaction.atomic():
                Thread(target=distanceCheck, args=(self.__dict__,)).start()
                oldReqNum = Request.objects.select_for_update(nowait=True).order_by('-requestNumber')[0]
                self.requestNumber = oldReqNum.requestNumber + 1
                super(Request, self).save(self, *args, **kwargs)
        else:
            super().save()

    def clean(self):
        geolocator = Nominatim(user_agent="Team Hawkeye")
        location = geolocator.geocode("{} {} {}".format(self.__dict__['address'], self.__dict__['city'], self.__dict__['state']))
        if (location == None):
            raise ValidationError({'address': ("This location combination does not exist"), 'city': ("This location combination does not exist"), 'state': ("This location combination does not exist"), 'zipCode': ("This location combination does not exist")})

    def get_absolute_url(self):
        return reverse('srDetail', kwargs={'pk': self.pk})

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requestId = models.ForeignKey(Request, on_delete=models.PROTECT)
    Sent = models.BooleanField(default=False)
    DateSent = models.DateTimeField(null=True,blank=True)

    class Meta:
        unique_together = (('user', 'requestId'),)
