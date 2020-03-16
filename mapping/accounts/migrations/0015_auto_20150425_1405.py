# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20150413_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshift',
            name='day_of_week',
            field=models.IntegerField(help_text='Day of week shift starts on.', verbose_name='day of week', default=1, choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')]),
        ),
    ]
