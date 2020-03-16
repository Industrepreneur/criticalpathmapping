# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_created', models.DateTimeField(null=True, auto_now_add=True)),
                ('date_updated', models.DateTimeField(null=True, auto_now=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, verbose_name='email address', help_text='Full email address, which acts as a primary, unique identifier.', max_length=255)),
                ('first_name', models.CharField(verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30)),
                ('is_active', models.BooleanField(default=True, verbose_name='active status', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('is_manager', models.BooleanField(default=False, verbose_name='manager status', help_text='Designates whether the user can manage users and other company-specific functionality.')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_created', models.DateTimeField(null=True, auto_now_add=True)),
                ('date_updated', models.DateTimeField(null=True, auto_now=True)),
                ('name', models.CharField(verbose_name='company name', max_length=150)),
                ('is_active', models.BooleanField(default=False, verbose_name='active status', help_text='Company status')),
                ('user_limit', models.SmallIntegerField(default=10, verbose_name='user limit', help_text='Max. number of users allowed', validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(help_text='Company this user belongs to', to='accounts.Company', null=True, related_name='users'),
            preserve_default=True,
        ),
    ]
