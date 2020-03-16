# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0012_auto_20150406_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='finished_goods_estimate',
            field=models.DecimalField(help_text='Time estimate for finished goods (in days)', verbose_name='finished goods estimate', max_digits=5, decimal_places=2, null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='logistics_estimate',
            field=models.DecimalField(help_text='Time estimate for logistics (in days)', verbose_name='logistics estimate', max_digits=5, decimal_places=2, null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='office_estimate',
            field=models.DecimalField(help_text='Time estimate for office tasks (in days)', verbose_name='office estimate', max_digits=5, decimal_places=2, null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='raw_materials_estimate',
            field=models.DecimalField(help_text='Time estimate for raw materials (in days)', verbose_name='raw materials estimate', max_digits=5, decimal_places=2, null=True),
        ),
    ]
