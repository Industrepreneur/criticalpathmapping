# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20150425_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshift',
            name='day_of_week',
            field=models.PositiveSmallIntegerField(help_text='Day of week shift starts on.', choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')], default=1, verbose_name='day of week'),
        ),
    ]
