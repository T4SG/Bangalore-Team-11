# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dream_site', '0009_auto_20150725_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals',
            name='goal_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 13, 57, 30, 769402), blank=True),
        ),
        migrations.AlterField(
            model_name='meetings',
            name='meeting_date',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_since',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
    ]
