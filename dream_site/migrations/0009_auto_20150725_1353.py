# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dream_site', '0008_auto_20150725_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentee',
            name='hobby',
            field=models.CharField(default='Reading', choices=[('Reading', 'Reading'), ('Sports', 'Sports'), ('Politics', 'Politics'), ('Computers', 'Computers'), ('Geography', 'Geography'), ('Wildlife', 'Wildlife'), ('Dance', 'Dance'), ('Drawing', 'Drawing'), ('Acting', 'Acting'), ('Cooking', 'Cooking'), ('Writing', 'Writing'), ('Video Games', 'Video Games')], max_length=20),
        ),
        migrations.AddField(
            model_name='mentor',
            name='hobby',
            field=models.CharField(default='Reading', choices=[('Reading', 'Reading'), ('Sports', 'Sports'), ('Politics', 'Politics'), ('Computers', 'Computers'), ('Geography', 'Geography'), ('Wildlife', 'Wildlife'), ('Dance', 'Dance'), ('Drawing', 'Drawing'), ('Acting', 'Acting'), ('Cooking', 'Cooking'), ('Writing', 'Writing'), ('Video Games', 'Video Games')], max_length=20),
        ),
        migrations.AddField(
            model_name='team',
            name='team_since',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 13, 53, 25, 596757), blank=True),
        ),
        migrations.AlterField(
            model_name='goals',
            name='goal_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 13, 53, 25, 598053), blank=True),
        ),
        migrations.AlterField(
            model_name='meetings',
            name='meeting_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 13, 53, 25, 597431), blank=True),
        ),
    ]
