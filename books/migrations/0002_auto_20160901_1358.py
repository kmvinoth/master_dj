# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadataset',
            name='dataobject',
            field=models.ForeignKey(blank=True, null=True, to='books.DataObject'),
        ),
        migrations.AlterField(
            model_name='metadataset',
            name='deposit',
            field=models.ForeignKey(blank=True, null=True, to='books.Deposit'),
        ),
        migrations.AlterField(
            model_name='metadataset',
            name='klt',
            field=models.ForeignKey(blank=True, null=True, to='books.KeyLabelType'),
        ),
        migrations.AlterField(
            model_name='metadataset',
            name='project',
            field=models.ForeignKey(blank=True, null=True, to='books.Projects'),
        ),
    ]
