# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0008_auto_20160114_2207'),
        ('forum', '0002_auto_20160109_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='id_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Core.Information'),
            preserve_default=False,
        ),
    ]