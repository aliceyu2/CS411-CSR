from django import forms
from .models import Request
from localflavor.us.us_states import STATE_CHOICES


class createRequest(forms.ModelForm):
    reqNum = forms.IntegerField(required = True, label = "Request Number")
    creationDate = forms.DateField(required = True, label = "Request Creation Date")
    compDate = forms.DateField(required = False, label = "Request Completion Date")
    requestType = forms.ChoiceField(choices = [(1,"Pot Hole Request"),(1,"Abandoned Vehicle Request")], label = "Request Type")
    status = forms.CharField(max_length = 100,required = True, label = "Request Status")
    priority = forms.IntegerField(required = True, label = "Request Priority")
    address = forms.CharField(max_length = 255, required = True, label = "Address of the Service Request")
    city = forms.CharField(max_length = 255, required = True, label = "City of the Service Request")
    zipCode = forms.IntegerField(required = True, label = "Zip Code of the Service Request")
    state = forms.ChoiceField(choices = STATE_CHOICES,required = True, label = "State of the Service Request")

    class Meta:
        model = Request
        fields = ['reqNum', 'creationDate', 'compDate', 'requestType', 'status', 'priority', 'address', 'city', 'zipCode', 'state']