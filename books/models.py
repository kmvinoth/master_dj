from datetime import date

from django.contrib.auth.models import User
from django.db import models
from enumfields import Enum
from enumfields import EnumField
from .fields import DataTypeField
from .validators import *
from django.forms import ModelForm


# class StatusFlag(Enum):
#     OPEN = 'open'
#     CLOSED = 'closed'


class KeyLabelType(models.Model):

    TYPE_TEXT = 'text'
    TYPE_FLOAT = 'float'
    TYPE_INT = 'int'

    DATATYPE_CHOICES = (
        (TYPE_TEXT, "Text"),
        (TYPE_FLOAT, "Float"),
        (TYPE_INT, "Integer"))

    # Model fields are defined here
    key = models.CharField(max_length=100, blank=True, null=True)
    label = models.CharField(max_length=100)
    datatype = DataTypeField(max_length=10, choices=DATATYPE_CHOICES)

    def get_validators(self):
        """ Returns the appropriate validator function from :mod:`.validators` for the datatype
            :param self: """

        DATATYPE_VALIDATORS = {
            'text': validate_text,
            'float': validate_float,
            'int': validate_int,
            }

        validation_function = DATATYPE_VALIDATORS[self.datatype]
        return validation_function

    def validate_value(self, val):
        """ Check *value* against the validators returned by :meth:`get_validators` for this attribute.
        :param val:
        :param self:  """

        validator = self.get_validators()
        validator(val)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = "KeyLabelType"


# As of now only one organization (ZIB)
class Organization(models.Model):
    name       = models.CharField(max_length=100)
    identifier = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = "Organization"


class Projects(models.Model):
    name  = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Projects"


class Permissions(models.Model):
    permission = models.CharField(max_length=100)

    def __str__(self):
        return self.permission

    class Meta:
        verbose_name_plural = "Permissions"


class Roles(models.Model):
    role        = models.CharField(max_length=100)
    permissions = models.ForeignKey(Permissions)

    def __str__(self):
        return self.role

    class Meta:
        verbose_name_plural = "Roles"


class ProjectMember(models.Model):
    project = models.ForeignKey(Projects, blank=True, null=True)
    user    = models.ForeignKey(User, blank=True, null=True)
    role    = models.ForeignKey(Roles, blank=True, null=True)

    # def __str__(self):
    #     return self.project

    class Meta:
        verbose_name_plural = "ProjectMember"


class Deposit(models.Model):
    project = models.ForeignKey(Projects)

    def __str__(self):
        return str(self.project)

    class Meta:
        verbose_name_plural = "Deposit"


class DataObject(models.Model):
    deposit = models.ForeignKey(Deposit)

    def __str__(self):
        return str(self.deposit)

    class Meta:
        verbose_name_plural = "DataObject"


class MetadataSet(models.Model):

    # Model fields are defined here
    project    = models.ForeignKey(Projects, blank=True, null=True)
    deposit    = models.ForeignKey(Deposit, blank=True, null=True)
    dataobject = models.ForeignKey(DataObject, blank=True, null=True)
    klt        = models.ForeignKey(KeyLabelType, blank=True, null=True)

    def __str__(self):
        return str(self.project)

    class Meta:
        verbose_name_plural = "MetadataSet"


class Value(models.Model):

    # Model fields are defined here
    metadataset        = models.ForeignKey(MetadataSet)
    value_text         = models.CharField(blank=True, null=True, default=None, max_length=100)
    value_int          = models.IntegerField(blank=True, null=True, default=None)
    value_float        = models.DecimalField(blank=True, null=True, default=None, max_digits=6, decimal_places=4)

    def __str__(self):
        return str(self.metadataset)

    class Meta:
        verbose_name_plural = "Value"

# PrId            = models.CharField(max_length=100, blank=True, null=True)
# StartDate       = models.DateField(default=date.today, blank=True, null=True)
# EndDate         = models.DateField(default=date.today, blank=True, null=True)
# Status          = EnumField(StatusFlag, blank=True, null=True)
# ProjectHead     = models.CharField(max_length=100, blank=True, null=True)
# Description     = models.TextField(blank=True, null=True)
# Budget          = models.IntegerField(blank=True, null=True)
# Partners        = models.CharField(max_length=100, blank=True, null=True)
# FundingAgency   = models.CharField(max_length=100, blank=True, null=True)


class ProjectMemberForm(ModelForm):

    class Meta:
        model = ProjectMember
        fields = ['project', 'user', 'role']



