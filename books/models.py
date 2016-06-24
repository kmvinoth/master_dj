from django.db import models
from django.contrib.auth.models import User
from enumfields import EnumField
from enumfields import Enum


class AuthFlag(Enum):
    DJANGO_AUTH = '0'
    LDAP_AUTH   = '1'
    OAUTH       = '2'


class DjangoUser(models.Model):
    ldap_u = models.OneToOneField(User)
    which_auth = EnumField(AuthFlag, max_length=1, default='0')

    def __str__(self):
        return self.which_auth


class LdapUser(models.Model):
    ldap_u = models.OneToOneField(User)
    which_auth = EnumField(AuthFlag, max_length=1, default='1')

    def __str__(self):
        return self.which_auth


class OauthUser(models.Model):
    oauth_u = models.OneToOneField(User)
    which_auth = EnumField(AuthFlag, max_length=1, default='2')

    def __str__(self):
        return self.which_auth


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
