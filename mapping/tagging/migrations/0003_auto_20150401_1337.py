# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0002_auto_20150331_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operationtype',
            name='value_type',
        ),
        migrations.AddField(
            model_name='operation',
            name='value_type',
            field=models.CharField(verbose_name='value type', choices=[('VA', 'Value Add'), ('NVA', 'Non Value Add'), ('RNVA', 'Required, Non Value Add')], max_length=4, default='VA', help_text='Value type classification (Value Add, Non Value Add, Required, Non Value Add)'),
            preserve_default=True,
        ),
    ]
