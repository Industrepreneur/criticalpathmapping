# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_user_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expiration',
            field=models.DateTimeField(null=True, verbose_name='expiration date', help_text='Account expiration date.', blank=True),
        ),
    ]
