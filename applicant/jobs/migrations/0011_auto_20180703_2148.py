# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-07-03 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20180415_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='employmentstatus',
            name='work_skills',
            field=models.ManyToManyField(to='jobs.WorkSkill', verbose_name='Work related skills'),
        ),
    ]
