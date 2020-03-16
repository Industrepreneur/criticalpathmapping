# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0008_auto_20150401_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='quantity_out',
            field=models.IntegerField(help_text='The outgoing quantity', default=0, verbose_name='quantity out'),
            preserve_default=False,
        ),
    ]
