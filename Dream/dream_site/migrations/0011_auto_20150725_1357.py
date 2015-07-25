# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dream_site', '0010_auto_20150725_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals',
            name='goal_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
