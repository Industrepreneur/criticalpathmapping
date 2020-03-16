# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0006_auto_20150401_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='quantity_in',
            field=models.IntegerField(verbose_name='quantity in', default=0, help_text='The incoming quantity'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='operation',
            name='quantity_out',
            field=models.IntegerField(verbose_name='quantity out', default=0, help_text='The outgoing quantity'),
            preserve_default=False,
        ),
    ]
