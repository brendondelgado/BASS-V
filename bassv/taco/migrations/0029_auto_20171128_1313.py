# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-28 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taco', '0028_auto_20171127_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='ta',
            field=models.ManyToManyField(help_text='Select a TA for this course', to='taco.Ta'),
        ),
    ]
