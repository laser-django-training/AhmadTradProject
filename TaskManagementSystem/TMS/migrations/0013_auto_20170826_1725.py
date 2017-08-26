# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0012_auto_20170826_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtask',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='subtask',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='Title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='subtask',
            name='owner',
        ),
    ]