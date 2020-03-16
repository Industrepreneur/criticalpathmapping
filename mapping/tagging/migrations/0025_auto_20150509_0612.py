# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0024_auto_20150423_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='description',
            field=models.CharField(help_text='Operation description', blank=True, verbose_name='operation description', null=True, max_length=50),
        ),
    ]
