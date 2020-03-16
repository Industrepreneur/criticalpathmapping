# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0021_auto_20150411_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationtype',
            name='description',
            field=models.TextField(null=True, blank=True, help_text='Optional description for the operation type', verbose_name='operation type description'),
        ),
    ]
