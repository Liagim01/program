# Generated by Django 3.2.17 on 2023-02-07 10:00

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0228_scheduledeventexport_scheduledorganizerexport'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='payment_provider_stamp',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
