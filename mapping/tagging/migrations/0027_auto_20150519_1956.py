# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0026_auto_20150518_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='Sheet release date',
            field=models.DateTimeField(verbose_name='release date', null=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='date_completed',
            field=models.DateTimeField(verbose_name='end date', help_text='Operation end date', null=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='date_started',
            field=models.DateTimeField(verbose_name='start date', help_text='Operation start date', null=True),
        ),
    ]
