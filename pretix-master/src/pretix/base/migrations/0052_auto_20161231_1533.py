# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 15:33
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0051_auto_20161221_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkins', to='pretixbase.OrderPosition'),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='price_mode',
            field=models.CharField(choices=[('none', 'No effect'), ('set', 'Set product price to'), ('subtract', 'Subtract from product price'), ('percent', 'Reduce product price by (%)')], default='none', max_length=100, verbose_name='Price mode'),
        ),
    ]
