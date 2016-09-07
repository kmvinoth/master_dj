# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import books.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'DataObject',
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Deposit',
            },
        ),
        migrations.CreateModel(
            name='KeyLabelType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('key', models.CharField(blank=True, null=True, max_length=100)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('dataobject', models.ForeignKey(to='books.DataObject')),
                ('deposit', models.ForeignKey(to='books.Deposit')),
                ('klt', models.ForeignKey(to='books.KeyLabelType')),
            ],
            options={
                'verbose_name_plural': 'MetadataSet',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Identifier', models.CharField(blank=True, null=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Organization',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('value_text', models.CharField(default=None, blank=True, null=True, max_length=100)),
                ('value_int', models.IntegerField(default=None, blank=True, null=True)),
                ('value_float', models.DecimalField(max_digits=6, default=None, decimal_places=4, blank=True, null=True)),
                ('metadataset', models.ForeignKey(to='books.MetadataSet')),
            ],
            options={
                'verbose_name_plural': 'Value',
            },
        ),
        migrations.AddField(
            model_name='metadataset',
            name='project',
            field=models.ForeignKey(to='books.Projects'),
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
