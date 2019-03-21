from django import forms
from .models import Request


class createRequest(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['requestType', 'address', 'city', 'zipCode', 'state']