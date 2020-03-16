# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationmethod',
            name='use_work_period',
            field=models.BooleanField(default=False, help_text='Determines whether this specific operation method is calculated using work periods.', verbose_name='uses work period'),
            preserve_default=True,
        ),
    ]
