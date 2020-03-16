# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_workperiod_workshift'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='workperiod',
            table='accounts_work_period',
        ),
        migrations.AlterModelTable(
            name='workshift',
            table='accounts_work_shift',
        ),
    ]
