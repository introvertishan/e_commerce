# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-16 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField()),
                ('img', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('detail', models.TextField()),
            ],
        ),
    ]
