# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('mentor_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=254)),
                ('age', models.IntegerField(max_length=2)),
                ('native_city', models.CharField(max_length=254)),
                ('current_city', models.CharField(max_length=254)),
                ('gender', models.CharField(default='Male', choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=254)),
                ('company', models.CharField(max_length=254)),
                ('area', models.CharField(max_length=254)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('username', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=254)),
            ],
        ),
    ]
