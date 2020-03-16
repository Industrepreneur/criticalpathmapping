# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0017_auto_20150408_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(null=True, auto_now_add=True)),
                ('date_updated', models.DateTimeField(null=True, auto_now=True)),
                ('background_color', models.CharField(max_length=50, help_text='Color used to represent this item when rendering in MAPs and Pie charts.  Examples: #8e44ad, rgb(212, 48, 100), rgb(212, 48, 100, 0.8), hsla(145, 78%, 68%), or hsla(145, 78%, 68%, 0.5)', verbose_name='background color')),
                ('is_striped', models.BooleanField(default=False, help_text='Whether item is rendered with a stripe overlay in MAPs and Pie charts.', verbose_name='has stripes')),
            ],
            options={
                'db_table': 'tagging_chart_style',
            },
        ),
        migrations.RemoveField(
            model_name='operationtype',
            name='color',
        ),
        migrations.RemoveField(
            model_name='operationtype',
            name='is_striped',
        ),
        migrations.AddField(
            model_name='operationtype',
            name='chart_style',
            field=models.OneToOneField(null=True, to='tagging.ChartStyle', related_name='operation_type'),
        ),
    ]
