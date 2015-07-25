# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dream_site', '0012_auto_20150725_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('goal_id', models.AutoField(primary_key=True, serialize=False)),
                ('goal_name', models.CharField(max_length=254, default='')),
                ('goal_achieved', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], default=0)),
                ('goal_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('team_id', models.ForeignKey(to='dream_site.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('meeting_id', models.AutoField(primary_key=True, serialize=False)),
                ('mentor_meeting_rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], default=0)),
                ('mentee_meeting_rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], default=0)),
                ('meeting_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('meeting', models.CharField(choices=[('Telephone', 'Telephone'), ('Online', 'Online'), ('Face to Face', 'Face to Face')], max_length=15, default='Face to Face')),
                ('team_id', models.ForeignKey(to='dream_site.Team')),
            ],
        ),
        migrations.RemoveField(
            model_name='goals',
            name='team_id',
        ),
        migrations.RemoveField(
            model_name='meetings',
            name='team_id',
        ),
        migrations.DeleteModel(
            name='Goals',
        ),
        migrations.DeleteModel(
            name='Meetings',
        ),
    ]
