# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0009_auto_20170919_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='%Y%m%d52640'),
        ),
    ]
