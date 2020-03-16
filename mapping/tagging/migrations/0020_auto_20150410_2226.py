# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0019_auto_20150410_2138'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chartstyle',
            unique_together=set([('background_color', 'is_striped')]),
        ),
    ]
