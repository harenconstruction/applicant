# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-07-11 19:01
from __future__ import unicode_literals

from django.db import migrations
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0004_auto_20180711_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcategory',
            name='position',
            field=positions.fields.PositionField(default=0),
        ),
    ]
