# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-30 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0006_auto_20190722_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffregistration',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='studentregistration',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
    ]
