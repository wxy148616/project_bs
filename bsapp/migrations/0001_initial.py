# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-02 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('psw', models.CharField(max_length=16)),
                ('age', models.IntegerField()),
                ('qq', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ptwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]
