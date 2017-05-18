# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-18 00:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbehost', '0018_auto_20170409_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField()),
                ('score', models.IntegerField()),
                ('json', models.TextField()),
            ],
            options={
                'verbose_name': 'SBE Round Score',
                'verbose_name_plural': 'SBE Round Scores',
            },
        ),
        migrations.AlterField(
            model_name='game',
            name='finish',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Game Finish'),
        ),
        migrations.AlterField(
            model_name='game',
            name='host_default_ping_ratio',
            field=models.SmallIntegerField(default=50, verbose_name='Game Host Pinback Percent'),
        ),
        migrations.AlterField(
            model_name='game',
            name='mode',
            field=models.SmallIntegerField(default=0, verbose_name='Game Mode'),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Game Name'),
        ),
        migrations.AlterField(
            model_name='game',
            name='options_cool',
            field=models.SmallIntegerField(default=300, verbose_name='Game Cool Down'),
        ),
        migrations.AlterField(
            model_name='game',
            name='options_flag_percent',
            field=models.SmallIntegerField(default=60, verbose_name='Game Flag Percentage'),
        ),
        migrations.AlterField(
            model_name='game',
            name='options_ticket_percent',
            field=models.SmallIntegerField(default=65, verbose_name='Game Ticket Percentage'),
        ),
        migrations.AlterField(
            model_name='game',
            name='options_ticket_wait',
            field=models.SmallIntegerField(default=180, verbose_name='Game Ticket First Hold Time (Sec)'),
        ),
        migrations.AlterField(
            model_name='game',
            name='paused',
            field=models.BooleanField(default=False, verbose_name='Game Pause'),
        ),
        migrations.AlterField(
            model_name='game',
            name='start',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Game Start'),
        ),
        migrations.AlterField(
            model_name='gamecompromise',
            name='finish',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Compromise End'),
        ),
        migrations.AlterField(
            model_name='gamecompromise',
            name='start',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Compromise Start'),
        ),
        migrations.AlterField(
            model_name='gamecontent',
            name='connect_status',
            field=models.CharField(blank=True, choices=[('1', 'success'), ('2', 'reset'), ('3', 'timeout')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='gamecontent',
            name='content_type',
            field=models.CharField(default='text', max_length=75, verbose_name='Content Type'),
        ),
        migrations.AlterField(
            model_name='gamecontent',
            name='data',
            field=models.TextField(blank=True, null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='gamecontent',
            name='http_verb',
            field=models.CharField(blank=True, choices=[('1', 'GET'), ('2', 'POST')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='gamedns',
            name='address',
            field=models.CharField(max_length=140, verbose_name='DNS Server Address'),
        ),
        migrations.AlterField(
            model_name='gameflag',
            name='answer',
            field=models.CharField(max_length=500, verbose_name='Flag Answer'),
        ),
        migrations.AlterField(
            model_name='gameflag',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Flag Name'),
        ),
        migrations.AlterField(
            model_name='gameflag',
            name='options',
            field=models.SmallIntegerField(default=2, verbose_name='Flag Options'),
        ),
        migrations.AlterField(
            model_name='gameflag',
            name='value',
            field=models.SmallIntegerField(default=100, verbose_name='Flag Value'),
        ),
        migrations.AlterField(
            model_name='gamehost',
            name='fqdn',
            field=models.CharField(max_length=250, verbose_name='Host Name'),
        ),
        migrations.AlterField(
            model_name='gamehost',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Host VM Name'),
        ),
        migrations.AlterField(
            model_name='gamehost',
            name='ping_ratio',
            field=models.SmallIntegerField(default=0, verbose_name='Host Pingback Percentage'),
        ),
        migrations.AlterField(
            model_name='gamehost',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Host Online (status)'),
        ),
        migrations.AlterField(
            model_name='gamehost',
            name='used',
            field=models.BooleanField(default=False, verbose_name='Host in Game (used)'),
        ),
        migrations.AlterField(
            model_name='gameplayer',
            name='score',
            field=models.IntegerField(default=0, verbose_name='Player Current Score'),
        ),
        migrations.AlterField(
            model_name='gameservice',
            name='bonus',
            field=models.BooleanField(default=False, verbose_name='Service is Bonus'),
        ),
        migrations.AlterField(
            model_name='gameservice',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Service Name'),
        ),
        migrations.AlterField(
            model_name='gameservice',
            name='status',
            field=models.CharField(choices=[('1', 'success'), ('2', 'reset'), ('3', 'timeout')], default='1', max_length=16, verbose_name='Service Status'),
        ),
        migrations.AlterField(
            model_name='gameservice',
            name='value',
            field=models.SmallIntegerField(default=50, verbose_name='Service Value'),
        ),
        migrations.AlterField(
            model_name='gameteam',
            name='score_basic',
            field=models.IntegerField(default=0, verbose_name='Team Score (Uptime)'),
        ),
        migrations.AlterField(
            model_name='gameteam',
            name='score_beacons',
            field=models.IntegerField(default=0, verbose_name='Team Score (Becons)'),
        ),
        migrations.AlterField(
            model_name='gameteam',
            name='score_flags',
            field=models.IntegerField(default=0, verbose_name='Team Score (Flags)'),
        ),
        migrations.AlterField(
            model_name='gameteam',
            name='score_tickets',
            field=models.IntegerField(default=0, verbose_name='Team Score (Tickets)'),
        ),
        migrations.AlterField(
            model_name='gameticket',
            name='completed',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ticket Completed'),
        ),
        migrations.AlterField(
            model_name='gameticket',
            name='content',
            field=models.CharField(max_length=1000, verbose_name='Ticket Body Content'),
        ),
        migrations.AlterField(
            model_name='gameticket',
            name='expired',
            field=models.BooleanField(default=False, verbose_name='Ticket Expired'),
        ),
        migrations.AlterField(
            model_name='gameticket',
            name='expires',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ticket Expires'),
        ),
        migrations.AlterField(
            model_name='gameticket',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Ticket Name'),
        ),
        migrations.AlterField(
            model_name='gameticket',
            name='started',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ticket Assigned'),
        ),
        migrations.AlterField(
            model_name='gameticket',
            name='value',
            field=models.SmallIntegerField(default=500, verbose_name='Ticket Value'),
        ),
        migrations.AlterField(
            model_name='serviceapplication',
            name='application_protocol',
            field=models.CharField(default='http', max_length=64, verbose_name='Application Protocol'),
        ),
        migrations.AlterField(
            model_name='serviceapplication',
            name='layer4_protocol',
            field=models.CharField(default='tcp', max_length=4, verbose_name='Service Protocol'),
        ),
        migrations.AlterField(
            model_name='serviceapplication',
            name='port',
            field=models.SmallIntegerField(default=0, verbose_name='Service Port'),
        ),
        migrations.AddField(
            model_name='gamescore',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbehost.Game'),
        ),
        migrations.AddField(
            model_name='gamescore',
            name='game_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbehost.GameService'),
        ),
        migrations.AddField(
            model_name='gamescore',
            name='game_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbehost.GameTeam'),
        ),
    ]
