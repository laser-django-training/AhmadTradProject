# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0007_auto_20170826_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtask',
            name='Title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subtask',
            name='progress',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='Title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='progress',
            field=models.IntegerField(default=0),
        ),
    ]