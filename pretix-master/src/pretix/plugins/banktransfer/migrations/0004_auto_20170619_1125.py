# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 11:25
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0062_auto_20170602_0948'),
        ('banktransfer', '0003_banktransaction_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankimportjob',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pretixbase.Organizer'),
        ),
        migrations.AddField(
            model_name='banktransaction',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pretixbase.Organizer'),
        ),
        migrations.AlterField(
            model_name='bankimportjob',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pretixbase.Event'),
        ),
        migrations.AlterField(
            model_name='banktransaction',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pretixbase.Event'),
        ),
        migrations.AlterUniqueTogether(
            name='banktransaction',
            unique_together=set([('event', 'organizer', 'checksum')]),
        ),
    ]
