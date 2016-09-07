
"""
**********
validators
**********

This module contains a validator for each Attribute datatype.

A validator is a callable that takes a value and raises a ``ValidationError``
if it doesn’t meet some criteria. (see `django validators at
<http://docs.djangoproject.com/en/dev/ref/validators/>`_)"""

from django.db import models
from django.core.exceptions import ValidationError


def validate_text(value):

    """ Raises ``ValidationError`` unless *value* type is ``str``
    :param value:
    """

    if not (type(value) == str):
        raise ValidationError("Must be string")


def validate_float(value):

    """ Raises ``ValidationError`` unless *value* can be cast as a ``float``
    :param value:
    """
    try:
        float(value)
    except ValueError:
        raise ValidationError("Must be a float")


def validate_int(value):

    """ Raises ``ValidationError`` unless *value* can be cast as an ``int``
    :param value:
    """
    try:
        int(value)
    except ValueError:
        raise ValidationError("Must be an integer")

