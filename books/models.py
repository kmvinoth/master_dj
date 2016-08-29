from datetime import date

from django.contrib.auth.models import User
from django.db import models
from enumfields import Enum
from enumfields import EnumField


class StatusFlag(Enum):
    OPEN = 'open'
    CLOSED = 'closed'


# As of now only one organization (ZIB)
class Organization(models.Model):
    Name       = models.CharField(max_length=100)
    Identifier = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Name


class Klt(models.Model):
    label = models.CharField(max_length=100)
    key   = models.CharField(max_length=100)
    value = models.CharField(max_length=100,blank=True, null=True)
    type  = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class Projects(models.Model):
    Name            = models.CharField(max_length=100)
    PrId            = models.CharField(max_length=100, blank=True, null=True)
    StartDate       = models.DateField(default=date.today, blank=True, null=True)
    EndDate         = models.DateField(default=date.today, blank=True, null=True)
    Status          = EnumField(StatusFlag, blank=True, null=True)
    ProjectHead     = models.CharField(max_length=100, blank=True, null=True)
    Description     = models.TextField(blank=True, null=True)
    organization    = models.ForeignKey(Organization)
    # Budget          = models.IntegerField(blank=True, null=True)
    # Partners        = models.CharField(max_length=100, blank=True, null=True)
    # FundingAgency   = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Name


class PrMdSet(models.Model):
    project    = models.ForeignKey(Projects)
    klt        = models.ForeignKey(Klt)

    def __str__(self):
        return str(self.project)


class Deposit(models.Model):
    project = models.ForeignKey(Projects)

    def __str__(self):
        return str(self.project)


class DepositMdSet(models.Model):
    project    = models.ForeignKey(Projects)
    deposit    = models.ForeignKey(Deposit)
    klt        = models.ForeignKey(Klt)

    def __str__(self):
        return str(self.deposit)


class DataObject(models.Model):
    deposit = models.ForeignKey(Deposit)

    def __str__(self):
        return str(self.deposit)


class DataObjectMdSet(models.Model):
    deposit       = models.ForeignKey(Deposit)
    dataobject    = models.ForeignKey(DataObject)
    klt           = models.ForeignKey(Klt)

    def __str__(self):
        return str(self.dataobject)









