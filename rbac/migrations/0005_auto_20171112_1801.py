# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20171110_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='rbac.Permission', verbose_name='拥有权限的角色3'),
        ),
    ]