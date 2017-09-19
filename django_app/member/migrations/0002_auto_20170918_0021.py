# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('D', 'Django'), ('F', 'Facebook'), ('N', 'Naver')], default='D', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]