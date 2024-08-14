from django import forms

# from .models import Booking
from django.core import validators
from django.contrib.auth.models import User
from MyDjango_App.models import WebPage, UserProfileInfo


def value_starts_Z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Enter name starts with Z !!!')


class FormName(forms.Form):
    # name = forms.CharField(validators=[validators.MinLengthValidator(3, "Minimum 3 Or more required")])
    name = forms.CharField(validators=[value_starts_Z])

    email = forms.EmailField()
    verify_email = forms.EmailField(label="Verify Email")
    desc = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_cleaned_data = super().clean()
        _email = all_cleaned_data['email']
        _verify_email = all_cleaned_data['verify_email']

        if _email != _verify_email:
            raise forms.ValidationError("Email no matches!!")
        return all_cleaned_data


class WebPage1(forms.ModelForm):
    class Meta:
        model = WebPage
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = {"username", "email", "password"}


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = {"portfolio_site", "profile_pic"}
