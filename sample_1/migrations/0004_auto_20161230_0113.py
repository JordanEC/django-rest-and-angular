# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-30 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_1', '0003_auto_20161229_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='sample_1.Author'),
        ),
    ]
