# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-17 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockscreener', '0004_batch_run'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch_run',
            name='mnemo',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='batch_run',
            name='web_source',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]