# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 10:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0006_auto_20171112_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='permissions',
        ),
    ]