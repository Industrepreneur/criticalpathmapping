# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0013_auto_20150406_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='date_setup_completed',
        ),
        migrations.RemoveField(
            model_name='operation',
            name='date_setup_started',
        ),
    ]
