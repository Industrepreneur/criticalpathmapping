# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0027_auto_20150519_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sheet',
            name='Sheet release date',
        ),
        migrations.AddField(
            model_name='sheet',
            name='release_date',
            field=models.DateTimeField(help_text='Sheet release date', verbose_name='release date', null=True),
        ),
    ]
