from django import forms
from django.forms import widgets
from .models import User


class LdapLoginForm(forms.Form):
    # make sure ldap login (username) is only Char
    ldap_login    = forms.CharField(max_length=100)
    ldap_password = forms.CharField(widget=forms.PasswordInput)

    # def clean_ldap_login(self):
    #     ldap_login = self.cleaned_data['ldap_login']
    #     empty      = ''
    #     if ldap_login is empty:
    #         raise forms.ValidationError("Missing ldap login credential")
    #     return ldap_login
    #
    # def clean_ldap_password(self):
    #     ldap_password = self.cleaned_data['ldap_password']
    #     empty    = ''
    #     if ldap_password is empty:
    #         raise forms.ValidationError("Missing ldap password")
    #     return ldap_password
    #
    #
    #
