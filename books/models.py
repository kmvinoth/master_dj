from datetime import date

from django.contrib.auth.models import User
from django.db import models
from enumfields import Enum
from enumfields import EnumField
# import eav
# from eav.models import Attribute


class StatusFlag(Enum):
    OPEN = 'open'
    CLOSED = 'closed'


# As of now only one organization (ZIB)
class Organization(models.Model):
    Name       = models.CharField(max_length=100)
    Identifier = models.CharField(max_length=100)


class ProjectMdSet(models.Model):
    label     = models.CharField(max_length=100)


class DepositMdSet(models.Model):
    l1       = models.CharField(max_length=100)


class DataObjectMdSet(models.Model):
    l2      = models.CharField(max_length=100)


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
    mdset_project   = models.ForeignKey(ProjectMdSet)


class Deposit(models.Model):
    mdset_deposit = models.ForeignKey(DepositMdSet)
    depo          = models.ForeignKey(Projects)


class DataObject(models.Model):
    mdset_data_object = models.ForeignKey(DataObjectMdSet)
    obj               = models.ForeignKey(Deposit)


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)





