# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 07:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0058_auto_20170528_0520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curriculumarea',
            options={'ordering': ['number', 'name']},
        ),
        migrations.AlterModelOptions(
            name='learningoutcome',
            options={'ordering': ['curriculum_areas__ordering', 'text']},
        ),
    ]
