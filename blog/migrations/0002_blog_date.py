# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(null=True, verbose_name='\u63d0\u4ea4\u65e5\u671f'),
        ),
    ]
