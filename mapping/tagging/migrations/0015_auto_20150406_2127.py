# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0014_auto_20150406_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='date_operation_completed',
            new_name='date_completed',
        ),
        migrations.RenameField(
            model_name='operation',
            old_name='date_operation_started',
            new_name='date_started',
        ),
    ]
