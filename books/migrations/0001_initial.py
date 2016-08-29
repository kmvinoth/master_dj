# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import enumfields.fields
import datetime
import books.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataObject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataObjectMdSet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('dataobject', models.ForeignKey(to='books.DataObject')),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='DepositMdSet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('deposit', models.ForeignKey(to='books.Deposit')),
            ],
        ),
        migrations.CreateModel(
            name='Klt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('label', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(null=True, max_length=100, blank=True)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Name', models.CharField(max_length=100)),
                ('Identifier', models.CharField(null=True, max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrMdSet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('klt', models.ForeignKey(to='books.Klt')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Name', models.CharField(max_length=100)),
                ('PrId', models.CharField(null=True, max_length=100, blank=True)),
                ('StartDate', models.DateField(null=True, default=datetime.date.today, blank=True)),
                ('EndDate', models.DateField(null=True, default=datetime.date.today, blank=True)),
                ('Status', enumfields.fields.EnumField(enum=books.models.StatusFlag, null=True, max_length=10, blank=True)),
                ('ProjectHead', models.CharField(null=True, max_length=100, blank=True)),
                ('Description', models.TextField(null=True, blank=True)),
                ('organization', models.ForeignKey(to='books.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='prmdset',
            name='project',
            field=models.ForeignKey(to='books.Projects'),
        ),
        migrations.AddField(
            model_name='depositmdset',
            name='klt',
            field=models.ForeignKey(to='books.Klt'),
        ),
        migrations.AddField(
            model_name='depositmdset',
            name='project',
            field=models.ForeignKey(to='books.Projects'),
        ),
        migrations.AddField(
            model_name='deposit',
            name='project',
            field=models.ForeignKey(to='books.Projects'),
        ),
        migrations.AddField(
            model_name='dataobjectmdset',
            name='deposit',
            field=models.ForeignKey(to='books.Deposit'),
        ),
        migrations.AddField(
            model_name='dataobjectmdset',
            name='klt',
            field=models.ForeignKey(to='books.Klt'),
        ),
        migrations.AddField(
            model_name='dataobject',
            name='deposit',
            field=models.ForeignKey(to='books.Deposit'),
        ),
    ]
