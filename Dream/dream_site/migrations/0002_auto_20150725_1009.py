# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('dream_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=254)),
                ('password', models.CharField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('mentee_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=254)),
                ('age', models.IntegerField(default=0)),
                ('native_city', models.CharField(default='', max_length=254)),
                ('current_city', models.CharField(default='', max_length=254)),
                ('languages', models.CharField(default='', max_length=254)),
                ('hobbies', models.CharField(default='', max_length=254)),
                ('gender', models.CharField(default='Male', choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('college', models.CharField(default='', max_length=254)),
                ('phone_number', models.CharField(default='', max_length=20)),
                ('area', models.CharField(default='', max_length=254)),
                ('address', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=254)),
                ('college_degree', models.CharField(default='', max_length=254)),
                ('username', models.CharField(default='', max_length=254)),
                ('password', models.CharField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('message_exchange_frequency', models.PositiveSmallIntegerField(default=0)),
                ('mentor_response_time', models.PositiveSmallIntegerField(default=0)),
                ('mentee_response_time', models.PositiveSmallIntegerField(default=0)),
                ('mentee_id', models.ForeignKey(to='dream_site.Mentee')),
            ],
        ),
        migrations.AddField(
            model_name='mentor',
            name='address',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='mentor',
            name='college_degree',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='mentor',
            name='hobbies',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='mentor',
            name='languages',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='area',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='company',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='current_city',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='email',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='name',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='native_city',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='password',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], default=0),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='username',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='team',
            name='mentor_id',
            field=models.ForeignKey(to='dream_site.Mentor'),
        ),
    ]
