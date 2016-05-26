# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminstrativeMetaData',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('SubmittingOrganization', models.CharField(max_length=80)),
                ('OrganizationIdentifier', models.CharField(max_length=80)),
                ('ContractNumber', models.CharField(max_length=80)),
                ('Contact', models.CharField(max_length=80)),
                ('ContactEmail', models.EmailField(max_length=254)),
                ('TransferCurator', models.CharField(max_length=80)),
                ('TransferCuratorEMail', models.EmailField(max_length=254)),
                ('SubmissionName', models.CharField(max_length=80)),
                ('SubmissionDescription', models.TextField()),
                ('RightsDescription', models.TextField()),
                ('AccessRights', models.CharField(max_length=80)),
                ('License', models.CharField(max_length=80)),
                ('DataSourceSystem', models.CharField(max_length=80)),
                ('MetadataFile', models.CharField(max_length=80)),
                ('MetadataFileFormat', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='DataUpload',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Title_dataset', models.CharField(max_length=80)),
                ('Author', models.CharField(max_length=30)),
                ('CreationDate', models.DateField()),
                ('Department', models.CharField(max_length=30)),
                ('Funder', models.CharField(max_length=30)),
                ('Project', models.CharField(max_length=30)),
                ('Abstract_dataset', models.TextField()),
                ('Methodology', models.TextField()),
            ],
        ),
    ]
