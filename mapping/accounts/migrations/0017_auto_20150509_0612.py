# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20150508_1648'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workshift',
            options={'ordering': ['day_of_week', 'time_shift_starts']},
        ),
    ]
