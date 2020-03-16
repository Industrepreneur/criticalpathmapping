# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0018_auto_20150409_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationtype',
            name='chart_style',
            field=models.ForeignKey(related_name='operation_type', to='tagging.ChartStyle', null=True),
        ),
    ]
