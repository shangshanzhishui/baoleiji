# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-10-25 12:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0004_auto_20181025_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bind_host',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='host_group',
        ),
        migrations.AddField(
            model_name='hostgroup',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
