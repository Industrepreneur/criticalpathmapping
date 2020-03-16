# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_workperiod_workshift'),
        ('tagging', '0003_auto_20150401_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='work_period',
            field=models.ForeignKey(default=1, to='accounts.WorkPeriod', related_name='operations'),
            preserve_default=False,
        ),
    ]
