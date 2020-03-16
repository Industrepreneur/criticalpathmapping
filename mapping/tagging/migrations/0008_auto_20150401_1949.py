# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0007_auto_20150401_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='quantity_in',
            field=models.IntegerField(null=True, help_text='The incoming quantity', verbose_name='quantity in'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='quantity_out',
            field=models.IntegerField(null=True, help_text='The outgoing quantity', verbose_name='quantity out'),
            preserve_default=True,
        ),
    ]
