# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 19:57
from __future__ import unicode_literals

from django.db import migrations, models
import web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_remove_officefile_max_coor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officefile',
            name='file',
            field=models.FileField(upload_to='', validators=[web.validators.validate_file_extension]),
        ),
    ]
