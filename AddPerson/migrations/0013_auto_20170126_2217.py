# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 03:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AddPerson', '0012_auto_20170126_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addmissionsservice',
            old_name='service',
            new_name='addmissions_service',
        ),
    ]