# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-07-10 23:06
from __future__ import unicode_literals

from django.db import migrations, models
import pm.models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectphoto',
            name='photo',
            field=models.ImageField(blank=True, upload_to=pm.models.get_file_path),
        ),
    ]