# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20150814_0410'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='expiration',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 30, 6, 5, 45, 666414, tzinfo=utc), help_text='Account expiration date.', verbose_name='expiration date'),
            preserve_default=False,
        ),
    ]
