# Writing custom fields for the Datatype

from django.db import models
from django.core.exceptions import ValidationError


class DataTypeField(models.CharField):

    pass


class ValueField(models.CharField):

    pass

