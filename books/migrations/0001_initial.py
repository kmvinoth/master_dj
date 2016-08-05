# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import books.models
import datetime
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Authenticationbackend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('which_auth', enumfields.fields.EnumField(max_length=10, default='django_auth', enum=books.models.AuthFlag)),
                ('std_u', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Identifier', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('PrId', models.CharField(max_length=100)),
                ('StartDate', models.DateField(default=datetime.date.today)),
                ('EndDate', models.DateField(default=datetime.date.today)),
                ('Status', enumfields.fields.EnumField(max_length=10, enum=books.models.StatusFlag)),
                ('ProjectHead', models.CharField(max_length=100)),
                ('Partners', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('FundingAgency', models.CharField(max_length=100)),
                ('Budget', models.IntegerField()),
                ('organization', models.ForeignKey(to='books.Organization')),
            ],
        ),
    ]
