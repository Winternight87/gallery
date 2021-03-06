# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_title', models.CharField(max_length=200)),
                ('pic_text', models.TextField()),
                ('pic_image', models.ImageField(upload_to='blog/static/')),
                ('pic_date', models.DateTimeField()),
                ('pic_likes', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'picture',
            },
        ),
    ]
