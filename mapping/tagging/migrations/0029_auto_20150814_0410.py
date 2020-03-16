# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0028_auto_20150519_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationmethod',
            name='description',
            field=models.TextField(help_text='Optional description for the operation', blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='operationmethod',
            name='name',
            field=models.CharField(help_text='The name of the operation (Mill:3-Axis, Heat Treat, Anodize, Outside Processing, ...)', verbose_name='name', max_length=50),
        ),
        migrations.AlterField(
            model_name='operationmethod',
            name='use_work_period',
            field=models.BooleanField(help_text='Determines whether this specific operation method is calculated using work periods.', default=False, verbose_name='use work period'),
        ),
        migrations.AlterField(
            model_name='operationtype',
            name='description',
            field=models.TextField(help_text='Optional description for the operation type', blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='part',
            name='creator',
            field=models.ForeignKey(related_name='parts', help_text='Part creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
