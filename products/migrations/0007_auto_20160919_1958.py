# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20160916_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.AddField(
            model_name='selectedproduct',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.Order'),
            preserve_default=False,
        ),
    ]
