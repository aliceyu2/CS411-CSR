from django.db import models
from django.contrib.auth.models import User


class Request(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)

    def save(self, *args, **kwargs):
        super().save()