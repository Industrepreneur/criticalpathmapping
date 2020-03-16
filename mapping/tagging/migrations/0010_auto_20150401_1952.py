# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0009_auto_20150401_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='quantity_in',
            field=models.IntegerField(help_text='The incoming quantity', default=0, verbose_name='quantity in'),
            preserve_default=False,
        ),
    ]
