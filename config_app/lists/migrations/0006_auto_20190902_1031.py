# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-09-02 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20190831_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
    ]
