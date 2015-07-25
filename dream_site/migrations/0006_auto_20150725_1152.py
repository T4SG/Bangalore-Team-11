# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dream_site', '0005_auto_20150725_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentee',
            name='languages',
        ),
        migrations.AddField(
            model_name='mentee',
            name='other_languages',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='mentee',
            name='primary_language',
            field=models.CharField(choices=[('Assamese', 'Assamese'), ('Bengali', 'Bengali'), ('Gujarati', 'Gujarati'), ('Hindi', 'Hindi'), ('Kannada', 'Kannada'), ('Marathi', 'Marathi'), ('Punjabi', 'Punjabi'), ('Sanskrit', 'Sanskrit'), ('Tamil', 'Tamil'), ('Urdu', 'Urdu'), ('Telugu', 'Telugu'), ('English', 'English')], default='English', max_length=20),
        ),
        migrations.AddField(
            model_name='mentee',
            name='secondary_language',
            field=models.CharField(choices=[('Assamese', 'Assamese'), ('Bengali', 'Bengali'), ('Gujarati', 'Gujarati'), ('Hindi', 'Hindi'), ('Kannada', 'Kannada'), ('Marathi', 'Marathi'), ('Punjabi', 'Punjabi'), ('Sanskrit', 'Sanskrit'), ('Tamil', 'Tamil'), ('Urdu', 'Urdu'), ('Telugu', 'Telugu'), ('English', 'English')], default='English', max_length=20),
        ),
    ]
