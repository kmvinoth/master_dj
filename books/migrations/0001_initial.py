# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import books.fields


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
                ('dataobject', models.ForeignKey(to='books.DataObject', null=True, blank=True)),
                ('deposit', models.ForeignKey(to='books.Deposit', null=True, blank=True)),
                ('klt', models.ForeignKey(to='books.KeyLabelType', null=True, blank=True)),
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
            name='ProjectAdmin',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
            options={
                'verbose_name_plural': 'ProjectAdmin',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('admin', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('role', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Role',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('value_text', models.CharField(default=None, null=True, blank=True, max_length=100)),
                ('value_int', models.IntegerField(default=None, null=True, blank=True)),
                ('value_float', models.DecimalField(default=None, null=True, decimal_places=4, blank=True, max_digits=6)),
                ('metadataset', models.ForeignKey(to='books.MetadataSet')),
            ],
            options={
                'verbose_name_plural': 'Value',
            },
        ),
        migrations.AddField(
            model_name='projectadmin',
            name='project',
            field=models.ForeignKey(to='books.Projects'),
        ),
        migrations.AddField(
            model_name='projectadmin',
            name='role',
            field=models.ForeignKey(to='books.Roles'),
        ),
        migrations.AddField(
            model_name='projectadmin',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='metadataset',
            name='project',
            field=models.ForeignKey(to='books.Projects', null=True, blank=True),
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
