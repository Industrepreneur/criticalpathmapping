# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0022_auto_20150413_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationmethod',
            name='description',
            field=models.TextField(null=True, blank=True, verbose_name='method description', help_text='Optional description for the operation'),
        ),
    ]
