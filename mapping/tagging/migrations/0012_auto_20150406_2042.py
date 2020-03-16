# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0011_auto_20150404_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='finished_goods_estimate',
            field=models.DecimalField(default=0.0, null=True, max_digits=5, verbose_name='finished goods estimate', help_text='Time estimate for finished goods (in days)', decimal_places=2),
        ),
        migrations.AddField(
            model_name='sheet',
            name='logistics_estimate',
            field=models.DecimalField(default=0.0, null=True, max_digits=5, verbose_name='logistics estimate', help_text='Time estimate for logistics (in days)', decimal_places=2),
        ),
        migrations.AddField(
            model_name='sheet',
            name='office_estimate',
            field=models.DecimalField(default=0.0, null=True, max_digits=5, verbose_name='office estimate', help_text='Time estimate for office tasks (in days)', decimal_places=2),
        ),
        migrations.AddField(
            model_name='sheet',
            name='raw_materials_estimate',
            field=models.DecimalField(default=0.0, null=True, max_digits=5, verbose_name='raw materials estimate', help_text='Time estimate for raw materials (in days)', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='description',
            field=models.TextField(verbose_name='sheet description', null=True, help_text='Sheet Description'),
        ),
    ]
