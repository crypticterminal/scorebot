# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-24 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sbehost', '0001_initial'),
        ('sbegame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitorjob',
            name='job_host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbehost.GameHost'),
        ),
        migrations.AddField(
            model_name='monitorjob',
            name='job_monitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbegame.MonitorServer'),
        ),
    ]