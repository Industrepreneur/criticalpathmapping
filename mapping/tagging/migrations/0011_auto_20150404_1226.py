# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0010_auto_20150401_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='value_type',
        ),
        migrations.AddField(
            model_name='operationtype',
            name='value_type',
            field=models.CharField(max_length=4, choices=[('VA', 'Value Add'), ('NVA', 'Non Value Add'), ('RNVA', 'Required, Non Value Add')], verbose_name='value type', default='VA', help_text='Value type classification (Value Add, Non Value Add, Required, Non Value Add)'),
        ),
    ]
