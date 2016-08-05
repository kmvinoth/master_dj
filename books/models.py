from django.db import models
from django.contrib.auth.models import User
from enumfields import EnumField
from enumfields import Enum
from datetime import date


class AuthFlag(Enum):
    DJANGO_AUTH = 'django_auth'
    LDAP_AUTH   = 'ldap_auth'
    OAUTH       = 'o_auth'


class StatusFlag(Enum):
    OPEN = 'open'
    CLOSED = 'closed'


class Authenticationbackend(models.Model):
    std_u = models.OneToOneField(User)
    which_auth = EnumField(AuthFlag, default='django_auth')

    def __str__(self):
        return self.which_auth


# As of now only one organization (ZIB)
class Organization(models.Model):
    Name       = models.CharField(max_length=100)
    Identifier = models.CharField(max_length=100)


class Projects(models.Model):
    Name            = models.CharField(max_length=100)
    PrId            = models.CharField(max_length=100)
    StartDate       = models.DateField(default=date.today)
    EndDate         = models.DateField(default=date.today)
    Status          = EnumField(StatusFlag)
    ProjectHead     = models.CharField(max_length=100)
    Partners        = models.CharField(max_length=100)
    Description     = models.TextField()
    FundingAgency   = models.CharField(max_length=100)
    Budget          = models.IntegerField()
    organization    = models.ForeignKey(Organization)


class ProjectMetadataSet(models.Model):

    """ Mandatory meta data """
    """ Customary meta data """
    container = models.ForeignKey(Projects)
    key       = models.CharField(max_length=100)
    value     = models.CharField(max_length=100)
