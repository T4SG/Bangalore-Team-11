# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dream_site', '0006_auto_20150725_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='languages',
        ),
        migrations.AddField(
            model_name='mentor',
            name='other_languages',
            field=models.CharField(max_length=254, default=''),
        ),
        migrations.AddField(
            model_name='mentor',
            name='primary_language',
            field=models.CharField(max_length=20, default='English', choices=[('Assamese', 'Assamese'), ('Bengali', 'Bengali'), ('Gujarati', 'Gujarati'), ('Hindi', 'Hindi'), ('Kannada', 'Kannada'), ('Marathi', 'Marathi'), ('Punjabi', 'Punjabi'), ('Sanskrit', 'Sanskrit'), ('Tamil', 'Tamil'), ('Urdu', 'Urdu'), ('Telugu', 'Telugu'), ('English', 'English')]),
        ),
        migrations.AddField(
            model_name='mentor',
            name='secondary_language',
            field=models.CharField(max_length=20, default='English', choices=[('Assamese', 'Assamese'), ('Bengali', 'Bengali'), ('Gujarati', 'Gujarati'), ('Hindi', 'Hindi'), ('Kannada', 'Kannada'), ('Marathi', 'Marathi'), ('Punjabi', 'Punjabi'), ('Sanskrit', 'Sanskrit'), ('Tamil', 'Tamil'), ('Urdu', 'Urdu'), ('Telugu', 'Telugu'), ('English', 'English')]),
        ),
    ]
