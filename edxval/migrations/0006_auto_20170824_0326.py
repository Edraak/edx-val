# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 07:26
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edxval', '0005_videoimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursevideo',
            name='is_hidden',
            field=models.BooleanField(default=False, help_text='Hide video for course.'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_name',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(code='invalid profile_name', message='profile_name has invalid characters', regex='^[a-zA-Z0-9\\-_]*$')]),
        ),
        migrations.AlterField(
            model_name='subtitle',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='subtitle',
            name='fmt',
            field=models.CharField(choices=[('srt', 'SubRip'), ('sjson', 'SRT JSON')], db_index=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='video',
            name='edx_video_id',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(code='invalid edx_video_id', message='edx_video_id has invalid characters', regex='^[a-zA-Z0-9\\-_]*$')]),
        ),
    ]
