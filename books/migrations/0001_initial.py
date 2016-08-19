# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import enumfields.fields
import books.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
            ],
            options={
                'ordering': ('headline',),
            },
        ),
        migrations.CreateModel(
            name='DataObject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DataObjectMdSet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('l2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DepositMdSet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('l1', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Identifier', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMdSet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
                ('mdset_project', models.ForeignKey(to='books.ProjectMdSet')),
                ('organization', models.ForeignKey(to='books.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='deposit',
            name='depo',
            field=models.ForeignKey(to='books.Projects'),
        ),
        migrations.AddField(
            model_name='deposit',
            name='mdset_deposit',
            field=models.ForeignKey(to='books.DepositMdSet'),
        ),
        migrations.AddField(
            model_name='dataobject',
            name='mdset_data_object',
            field=models.ForeignKey(to='books.DataObjectMdSet'),
        ),
        migrations.AddField(
            model_name='dataobject',
            name='obj',
            field=models.ForeignKey(to='books.Deposit'),
        ),
        migrations.AddField(
            model_name='article',
            name='reporter',
            field=models.ForeignKey(to='books.Reporter'),
        ),
    ]
