from django.db import models
from django.core.validators import MinValueValidator

class profile(models.Model):
	emailAddress = models.CharField(max_length=300)
	watchList = models.TextField()
	radius = models.IntegerField()
	
	def __str__(self):
		return self.emailAddress

class serviceRequest(models.Model):
	requestNumber = models.PositiveIntegerField(validators=[MinValueValidator(1)])
	
	def __str__(self):
		return self.title