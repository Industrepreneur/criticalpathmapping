# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0016_auto_20150408_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationtype',
            name='color',
            field=models.CharField(default='hsla(282, 61%, 68%, 1)', verbose_name='chart color', help_text='Color used to represent this Operation Type when rendering in MAPs and Pie charts.  This can be #HHEEXX, rgb(), rgba(), hsl(), or hsla()', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operationtype',
            name='is_striped',
            field=models.BooleanField(default=True, verbose_name='has stripes', help_text='Whether Operation Type is rendered with a stripe overlay in MAPs and Pie charts.'),
        ),
    ]
