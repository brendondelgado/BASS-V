# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 23:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taco', '0006_course_cdescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentcommunication',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='messagecommunication',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='courseOfferingID',
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taco.Professor'),
        ),
    ]
