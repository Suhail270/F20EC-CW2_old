from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import User

User = get_user_model()


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'mobile',
            'organization',
            'domain',
        )

    def clean_first_name(self):
        data = self.cleaned_data["first_name"]
        return data

    def clean(self):
        pass

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}