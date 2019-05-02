from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from localflavor.us.us_states import STATE_CHOICES
from geopy.geocoders import Nominatim
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	def clean_email(self):
		email = self.cleaned_data.get('email')
		try:
			match = User.objects.get(email = email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('This email address is already in use!')
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['firstName', 'lastName', 'age', 'address', 'city', 'state', 'zipCode', 'profile_pic']
		labels = {
			"firstName": "First Name",
			"lastName": "Last Name",
			"address": "Address",
			"age": "Age",
			"city": "City",
			"state": "State",
			"zipCode": "Zip Code",
			"profile_pic": "Profile Picture"
		}
	
	def clean(self):
		data = self.cleaned_data
		geolocator = Nominatim(user_agent="Team Hawkeye")
		location = geolocator.geocode("{} {} {}".format(self.data['address'], self.data['city'], self.data['state']))
		if(location == None):
			self.add_error('address', "This location combination does not exist")
			self.add_error('city', "This location combination does not exist")
			self.add_error('state', "This location combination does not exist")
			self.add_error('zipCode', "This location combination does not exist")
		
		return data