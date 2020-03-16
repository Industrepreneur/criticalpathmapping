# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date_created', models.DateTimeField(null=True, auto_now_add=True)),
                ('date_updated', models.DateTimeField(null=True, auto_now=True)),
                ('description', models.CharField(max_length=50, verbose_name='operation description', help_text='Operation description')),
                ('date_setup_started', models.DateTimeField(null=True)),
                ('date_setup_completed', models.DateTimeField(null=True)),
                ('date_operation_started', models.DateTimeField(null=True)),
                ('date_operation_completed', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OperationMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date_created', models.DateTimeField(null=True, auto_now_add=True)),
                ('date_updated', models.DateTimeField(null=True, auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='method name', help_text='The name of the operation (Mill:3-Axis, Heat Treat, Anodize, Outside Processing, ...)')),
                ('description', models.TextField(null=True, verbose_name='method description', help_text='Optional description for the operation')),
                ('use_work_period', models.BooleanField(default=True, verbose_name='uses work period', help_text='Determines whether this specific operation method is calculated using work periods.')),
                ('company', models.ForeignKey(to='accounts.Company', related_name='operation_methods')),
            ],
            options={
                'db_table': 'tagging_operation_method',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OperationType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date_created', models.DateTimeField(null=True, auto_now_add=True)),
                ('date_updated', models.DateTimeField(null=True, auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='operation type', unique=True, help_text='The type of operation')),
                ('description', models.TextField(null=True, verbose_name='operation type description', help_text='Optional description for the operation type')),
                ('value_type', models.CharField(max_length=4, default='VA', verbose_name='value type', choices=[('VA', 'Value Add'), ('NVA', 'Non Value Add'), ('RNVA', 'Required, Non Value Add')], help_text='Value type classification (Value Add, Non Value Add, Required, Non Value Add)')),
            ],
            options={
                'db_table': 'tagging_operation_type',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date_created', models.DateTimeField(null=True, auto_now_add=True)),
                ('date_updated', models.DateTimeField(null=True, auto_now=True)),
                ('name', models.CharField(max_length=150, verbose_name='part name', help_text='Part name')),
                ('description', models.TextField(null=True, verbose_name='part description', help_text='Part description')),
                ('creator', models.ForeignKey(to='accounts.User', help_text='Part owner', related_name='parts')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date_created', models.DateTimeField(null=True, auto_now_add=True)),
                ('date_updated', models.DateTimeField(null=True, auto_now=True)),
                ('description', models.TextField(null=True, help_text='Sheet Description')),
                ('creator', models.ForeignKey(to='accounts.User', related_name='sheets')),
                ('part', models.ForeignKey(to='tagging.Part', related_name='sheets')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='operation',
            name='operation_method',
            field=models.ForeignKey(to='tagging.OperationMethod', related_name='operations'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='operation',
            name='operation_type',
            field=models.ForeignKey(to='tagging.OperationType', related_name='operations'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='operation',
            name='sheet',
            field=models.ForeignKey(to='tagging.Sheet', related_name='operations'),
            preserve_default=True,
        ),
    ]
