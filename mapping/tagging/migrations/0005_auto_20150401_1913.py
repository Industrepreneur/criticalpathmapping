# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0004_operation_work_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='description',
            field=models.CharField(help_text='Operation description', null=True, verbose_name='operation description', max_length=50),
            preserve_default=True,
        ),
    ]
