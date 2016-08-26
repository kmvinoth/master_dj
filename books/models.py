from datetime import date

from django.contrib.auth.models import User
from django.db import models
from enumfields import Enum
from enumfields import EnumField
import eav


class StatusFlag(Enum):
    OPEN = 'open'
    CLOSED = 'closed'


# As of now only one organization (ZIB)
class Organization(models.Model):
    Name       = models.CharField(max_length=100)
    Identifier = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Name


class Projects(models.Model):
    Name            = models.CharField(max_length=100)
    # PrId            = models.CharField(max_length=100, blank=True, null=True)
    # StartDate       = models.DateField(default=date.today, blank=True, null=True)
    # EndDate         = models.DateField(default=date.today, blank=True, null=True)
    # Status          = EnumField(StatusFlag, blank=True, null=True)
    # ProjectHead     = models.CharField(max_length=100, blank=True, null=True)
    # Partners        = models.CharField(max_length=100, blank=True, null=True)
    # Description     = models.TextField(blank=True, null=True)
    # FundingAgency   = models.CharField(max_length=100, blank=True, null=True)
    # Budget          = models.IntegerField(blank=True, null=True)
    organization    = models.ForeignKey(Organization)

    def __str__(self):
        return self.Name


class Deposit(models.Model):
    project = models.ForeignKey(Projects)

    def __str__(self):
        return self.project


class DataObject(models.Model):
    deposit = models.ForeignKey(Deposit)

eav.register(Projects)
eav.register(Deposit)
eav.register(DataObject)







