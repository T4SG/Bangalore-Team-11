# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dream_site', '0007_auto_20150725_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('goal_id', models.AutoField(serialize=False, primary_key=True)),
                ('goal_name', models.CharField(default='', max_length=254)),
                ('goal_achieved', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('goal_date', models.DateTimeField(default=datetime.datetime(2015, 7, 25, 13, 19, 24, 376259), blank=True)),
                ('team_id', models.ForeignKey(to='dream_site.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('meeting_id', models.AutoField(serialize=False, primary_key=True)),
                ('mentor_meeting_rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('mentee_meeting_rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('meeting_date', models.DateTimeField(default=datetime.datetime(2015, 7, 25, 13, 19, 24, 375601), blank=True)),
                ('meeting', models.CharField(default='Face to Face', choices=[('Telephone', 'Telephone'), ('Online', 'Online'), ('Face to Face', 'Face to Face')], max_length=15)),
                ('team_id', models.ForeignKey(to='dream_site.Team')),
            ],
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='rating',
        ),
        migrations.AddField(
            model_name='mentee',
            name='number_of_ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mentor',
            name='number_of_ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mentor',
            name='rating_academics',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='mentor',
            name='rating_cocurricular',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='mentor',
            name='rating_communication',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='mentor',
            name='rating_overall',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
