# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0023_auto_20150413_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='finished_goods_estimate',
            field=models.DecimalField(max_digits=5, default=0, help_text='Time estimate for finished goods (in days)', decimal_places=2, verbose_name='finished goods estimate'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='logistics_estimate',
            field=models.DecimalField(max_digits=5, default=0, help_text='Time estimate for logistics (in days)', decimal_places=2, verbose_name='logistics estimate'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='office_estimate',
            field=models.DecimalField(max_digits=5, default=0, help_text='Time estimate for office tasks (in days)', decimal_places=2, verbose_name='office estimate'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='raw_materials_estimate',
            field=models.DecimalField(max_digits=5, default=0, help_text='Time estimate for raw materials (in days)', decimal_places=2, verbose_name='raw materials estimate'),
        ),
    ]
