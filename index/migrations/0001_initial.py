# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-15 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=100)),
                ('project_type', models.CharField(max_length=70)),
                ('project_cover_pic', models.ImageField(blank=True, upload_to='uploads/coverpics/')),
                ('client', models.CharField(blank=True, max_length=150)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('project_description', models.TextField(blank=True, max_length=500)),
                ('project_link', models.URLField(blank=True)),
            ],
        ),
    ]