# Generated by Django 3.2.3 on 2021-05-25 13:11

from django.db import migrations, models

import pretix.base.models.event
import pretix.base.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0188_delete_requiredaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='testmode',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='sales_channels',
            field=pretix.base.models.fields.MultiStringField(default=pretix.base.models.event.default_sales_channels),
        ),
    ]
