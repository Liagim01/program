# Generated by Django 3.2.16 on 2022-11-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0223_voucher_min_usages'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmetaproperty',
            name='filter_allowed',
            field=models.BooleanField(default=True),
        ),
    ]
