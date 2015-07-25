# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dream_site', '0004_auto_20150725_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentee',
            name='college_degree',
            field=models.CharField(max_length=50, choices=[('Computer Science Engineering', 'Computer Science Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Electronics Engineering', 'Electronics Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Biotechnology', 'Biotechnology'), ('Telecommunications Engineering', 'Telecommunications Engineering'), ('Physics Honours', 'Physics Honours'), ('Chemistry Honours', 'Chemistry Honours'), ('Economics', 'Economics'), ('Finance', 'Finance'), ('Accounting', 'Accounting'), ('Medicine', 'Medicine'), ('History Honours', 'History Honours'), ('Sociology Honours', 'Sociology Honours'), ('English Honours', 'English Honours')], default='Computer Science Engineering'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='college_degree',
            field=models.CharField(max_length=50, choices=[('Computer Science Engineering', 'Computer Science Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Electronics Engineering', 'Electronics Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Biotechnology', 'Biotechnology'), ('Telecommunications Engineering', 'Telecommunications Engineering'), ('Physics Honours', 'Physics Honours'), ('Chemistry Honours', 'Chemistry Honours'), ('Economics', 'Economics'), ('Finance', 'Finance'), ('Accounting', 'Accounting'), ('Medicine', 'Medicine'), ('History Honours', 'History Honours'), ('Sociology Honours', 'Sociology Honours'), ('English Honours', 'English Honours')], default='Computer Science Engineering'),
        ),
    ]
