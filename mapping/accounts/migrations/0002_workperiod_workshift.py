# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkPeriod',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(verbose_name='name', max_length=150, help_text='Work period name')),
                ('description', models.TextField(verbose_name='description', null=True, help_text='Work period description')),
                ('company', models.ForeignKey(to='accounts.Company', help_text='Company this work period belongs to', related_name='work_periods')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkShift',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('day_of_week', models.IntegerField(default=0, choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], verbose_name='day of week', help_text='Day of week shift starts on.')),
                ('time_shift_starts', models.TimeField(verbose_name='shift start time', help_text='Shift start')),
                ('time_shift_ends', models.TimeField(verbose_name='shift end time', help_text='Shift end')),
                ('work_period', models.ForeignKey(related_name='work_shifts', to='accounts.WorkPeriod')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
