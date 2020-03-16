# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0029_auto_20150814_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='description',
            field=models.TextField(blank=True, verbose_name='operation description', help_text='Operation description', null=True),
        ),
    ]
