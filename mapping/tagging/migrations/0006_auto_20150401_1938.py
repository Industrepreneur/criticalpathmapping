# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0005_auto_20150401_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='quantity_in',
            field=models.IntegerField(verbose_name='quantity in', help_text='The incoming quantity', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='operation',
            name='quantity_out',
            field=models.IntegerField(verbose_name='quantity out', help_text='The outgoing quantity', null=True),
            preserve_default=True,
        ),
    ]
