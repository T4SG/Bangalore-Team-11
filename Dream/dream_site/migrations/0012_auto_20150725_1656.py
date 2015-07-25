# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('dream_site', '0011_auto_20150725_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentee',
            name='hobbies',
        ),
        migrations.RemoveField(
            model_name='mentee',
            name='hobby',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='hobbies',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='hobby',
        ),
        migrations.AddField(
            model_name='mentee',
            name='hobby_1',
            field=models.CharField(default='Reading', choices=[('Reading', 'Reading'), ('Sports', 'Sports'), ('Politics', 'Politics'), ('Computers', 'Computers'), ('Geography', 'Geography'), ('Wildlife', 'Wildlife'), ('Dance', 'Dance'), ('Drawing', 'Drawing'), ('Acting', 'Acting'), ('Cooking', 'Cooking'), ('Writing', 'Writing'), ('Video Games', 'Video Games')], max_length=20),
        ),
        migrations.AddField(
            model_name='mentee',
            name='hobby_2',
            field=models.CharField(default='Reading', choices=[('Reading', 'Reading'), ('Sports', 'Sports'), ('Politics', 'Politics'), ('Computers', 'Computers'), ('Geography', 'Geography'), ('Wildlife', 'Wildlife'), ('Dance', 'Dance'), ('Drawing', 'Drawing'), ('Acting', 'Acting'), ('Cooking', 'Cooking'), ('Writing', 'Writing'), ('Video Games', 'Video Games')], max_length=20),
        ),
        migrations.AddField(
            model_name='mentee',
            name='hobby_3',
            field=models.CharField(default='Reading', choices=[('Reading', 'Reading'), ('Sports', 'Sports'), ('Politics', 'Politics'), ('Computers', 'Computers'), ('Geography', 'Geography'), ('Wildlife', 'Wildlife'), ('Dance', 'Dance'), ('Drawing', 'Drawing'), ('Acting', 'Acting'), ('Cooking', 'Cooking'), ('Writing', 'Writing'), ('Video Games', 'Video Games')], max_length=20),
        ),
        migrations.AddField(
            model_name='mentee',
            name='hobby_4',
            field=models.CharField(default='Reading', choices=[('Reading', 'Reading'), ('Sports', 'Sports'), ('Politics', 'Politics'), ('Computers', 'Computers'), ('Geography', 'Geography'), ('Wildlife', 'Wildlife'), ('Dance', 'Dance'), ('Drawing', 'Drawing'), ('Acting', 'Acting'), ('Cooking', 'Cooking'), ('Writing', 'Writing'), ('Video Games', 'Video Games')], max_length=20),
        ),
        migrations.AddField(
            model_name='mentor',
            name='hobby_1',
            field=models.CharField(default='Reading', choices=[('Reading', 'Reading'), ('Sports', 'Sports'), ('Politics', 'Politics'), ('Computers', 'Computers'), ('Geography', 'Geography'), ('Wildlife', 'Wildlife'), ('Dance', 'Dance'), ('Drawing', 'Drawing'), ('Acting', 'Acting'), ('Cooking', 'Cooking'), ('Writing', 'Writing'), ('Video Games', 'Video Games')], max_length=20),
        ),
        migrations.AddField(
            model_name='mentor',
            name='hobby_2',
            field=models.CharField(default='Reading', choices=[('Reading', 'Reading'), ('Sports', 'Sports'), ('Politics', 'Politics'), ('Computers', 'Computers'), ('Geography', 'Geography'), ('Wildlife', 'Wildlife'), ('Dance', 'Dance'), ('Drawing', 'Drawing'), ('Acting', 'Acting'), ('Cooking', 'Cooking'), ('Writing', 'Writing'), ('Video Games', 'Video Games')], max_length=20),
        ),
        migrations.AddField(
            model_name='mentor',
            name='hobby_3',
            field=models.CharField(default='Reading', choices=[('Reading', 'Reading'), ('Sports', 'Sports'), ('Politics', 'Politics'), ('Computers', 'Computers'), ('Geography', 'Geography'), ('Wildlife', 'Wildlife'), ('Dance', 'Dance'), ('Drawing', 'Drawing'), ('Acting', 'Acting'), ('Cooking', 'Cooking'), ('Writing', 'Writing'), ('Video Games', 'Video Games')], max_length=20),
        ),
        migrations.AddField(
            model_name='mentor',
            name='hobby_4',
            field=models.CharField(default='Reading', choices=[('Reading', 'Reading'), ('Sports', 'Sports'), ('Politics', 'Politics'), ('Computers', 'Computers'), ('Geography', 'Geography'), ('Wildlife', 'Wildlife'), ('Dance', 'Dance'), ('Drawing', 'Drawing'), ('Acting', 'Acting'), ('Cooking', 'Cooking'), ('Writing', 'Writing'), ('Video Games', 'Video Games')], max_length=20),
        ),
        migrations.AlterField(
            model_name='mentee',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(35)]),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(90)]),
        ),
    ]
