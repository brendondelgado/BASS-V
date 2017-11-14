# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taco', '0012_auto_20171113_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ta',
            name='first_name',
        ),
        migrations.AddField(
            model_name='ta',
            name='full_name',
            field=models.CharField(default=1111, help_text='Enter Full Name', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='ta',
            field=models.ManyToManyField(help_text='Select a TA for this course', to='taco.Ta'),
        ),
    ]