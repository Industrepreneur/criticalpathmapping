# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20150412_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='workperiod',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='default period', help_text='Specifies whether this is the default Work Period.'),
        ),
        migrations.AlterField(
            model_name='company',
            name='user_limit',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], default=10, verbose_name='user limit', help_text='Max. number of users allowed'),
        ),
    ]
