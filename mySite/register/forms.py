from django import forms
from localflavor.us.us_states import STATE_CHOICES


class registerForm(forms.Form):
    email = forms.EmailField(label='Email Address', max_length=100)
    firstName = forms.CharField(label='First Name', max_length=100)
    lastName = forms.CharField(label='Last Name', max_length=100)
    street = forms.CharField(label='Address', max_length=100)
    city =  forms.ChoiceField(choices = STATE_CHOICES)
    zip = forms.CharField(label='Zip Code', max_length=100)
    password = forms.CharField(max_length=32,label = "Password", widget=forms.PasswordInput)
    verifyPassword  = forms.CharField(max_length=32,label = "Verify Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(registerForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("verifyPassword")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )