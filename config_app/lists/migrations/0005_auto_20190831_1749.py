# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-08-31 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20190825_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default='', null=True),
        ),
    ]