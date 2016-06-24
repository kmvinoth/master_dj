from django import forms
from .models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if username is not None:
            return username
        else:
            raise forms.ValidationError("Enter a valid username")

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if password is not None:
            return password
        else:
            raise forms.ValidationError("Enter a valid password")
