# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 18:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vereniging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gebruiker',
            name='vereniging',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vereniging.ZeilVereniging'),
        ),
    ]
