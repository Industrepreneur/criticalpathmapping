# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20150509_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='is_active',
            field=models.BooleanField(help_text='Company status', default=False, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(help_text='Whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(help_text='Whether the user can manage all companies, users, and operation types.', default=False, verbose_name='admin'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(help_text='Whether the user can manage users and other company-specific functionality.', default=False, verbose_name='manager'),
        ),
    ]
