# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_selectedproduct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='selectedproduct',
            options={'ordering': ('date',)},
        ),
        migrations.AddField(
            model_name='selectedproduct',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
