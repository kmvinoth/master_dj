# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import books.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataObject',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
            options={
                'verbose_name_plural': 'DataObject',
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
            options={
                'verbose_name_plural': 'Deposit',
            },
        ),
        migrations.CreateModel(
            name='KeyLabelType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('key', models.CharField(null=True, blank=True, max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('datatype', books.fields.DataTypeField(choices=[('text', 'Text'), ('float', 'Float'), ('int', 'Integer')], max_length=10)),
            ],
            options={
                'verbose_name_plural': 'KeyLabelType',
            },
        ),
        migrations.CreateModel(
            name='MetadataSet',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('dataobject', models.ForeignKey(blank=True, to='books.DataObject', null=True)),
                ('deposit', models.ForeignKey(blank=True, to='books.Deposit', null=True)),
                ('klt', models.ForeignKey(blank=True, to='books.KeyLabelType', null=True)),
            ],
            options={
                'verbose_name_plural': 'MetadataSet',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('identifier', models.CharField(null=True, blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Organization',
            },
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('permission', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Permissions',
            },
        ),
        migrations.CreateModel(
            name='ProjectMember',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
            options={
                'verbose_name_plural': 'ProjectMember',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('role', models.CharField(max_length=100)),
                ('permissions', models.ForeignKey(to='books.Permissions')),
            ],
            options={
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('value_text', models.CharField(null=True, default=None, blank=True, max_length=100)),
                ('value_int', models.IntegerField(default=None, blank=True, null=True)),
                ('value_float', models.DecimalField(default=None, max_digits=6, blank=True, decimal_places=4, null=True)),
                ('metadataset', models.ForeignKey(to='books.MetadataSet')),
            ],
            options={
                'verbose_name_plural': 'Value',
            },
        ),
        migrations.AddField(
            model_name='projectmember',
            name='project',
            field=models.ForeignKey(blank=True, to='books.Projects', null=True),
        ),
        migrations.AddField(
            model_name='projectmember',
            name='role',
            field=models.ForeignKey(blank=True, to='books.Roles', null=True),
        ),
        migrations.AddField(
            model_name='projectmember',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='metadataset',
            name='project',
            field=models.ForeignKey(blank=True, to='books.Projects', null=True),
        ),
        migrations.AddField(
            model_name='deposit',
            name='project',
            field=models.ForeignKey(to='books.Projects'),
        ),
        migrations.AddField(
            model_name='dataobject',
            name='deposit',
            field=models.ForeignKey(to='books.Deposit'),
        ),
    ]
