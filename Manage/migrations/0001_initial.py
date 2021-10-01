# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-24 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('credit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='trnf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cfrom', models.CharField(max_length=30)),
                ('cto', models.CharField(max_length=30)),
                ('credit', models.IntegerField()),
            ],
        ),
    ]