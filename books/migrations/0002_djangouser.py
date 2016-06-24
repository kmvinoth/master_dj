# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import enumfields.fields
import books.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('which_auth', enumfields.fields.EnumField(max_length=1, enum=books.models.AuthFlag)),
                ('ldap_u', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
