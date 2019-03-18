from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from localflavor.us.us_states import STATE_CHOICES


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username']

class ProfileUpdateForm(forms.ModelForm):
	firstName = forms.CharField(max_length=100, required=False, label="First Name")
	lastName = forms.CharField(max_length=100, required=False, label="Last Name")
	address = forms.CharField(max_length=255, required=False, label="Address")
	city = forms.CharField(max_length=100, required=False, label="City")
	state = forms.ChoiceField(choices=STATE_CHOICES, required=False, label="State")
	zip = forms.CharField(max_length=5, required=False, label="Zip Code")
	class Meta:
		model = Profile
		fields = ['firstName', 'lastName', 'address', 'city', 'state', 'zip', 'profile_pic']