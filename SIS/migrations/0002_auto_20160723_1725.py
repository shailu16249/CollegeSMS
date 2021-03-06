# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-23 11:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SIS', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='user',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AddField(
            model_name='faculty',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='password',
            field=models.CharField(default=datetime.datetime(2016, 7, 23, 11, 55, 8, 742570, tzinfo=utc), max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=30, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
