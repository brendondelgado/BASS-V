# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taco', '0020_auto_20171123_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='ta',
            field=models.ManyToManyField(help_text='Select a TA for this course', to='taco.Ta'),
        ),
    ]
