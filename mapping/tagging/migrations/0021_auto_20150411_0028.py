# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0020_auto_20150410_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='quantity_in',
            field=models.PositiveIntegerField(help_text='The incoming quantity', verbose_name='quantity in'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='quantity_out',
            field=models.PositiveIntegerField(help_text='The outgoing quantity', verbose_name='quantity out'),
        ),
    ]
