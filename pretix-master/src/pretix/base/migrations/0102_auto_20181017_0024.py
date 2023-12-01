# Generated by Django 2.1 on 2018-10-17 00:24


from django.core.exceptions import ImproperlyConfigured
from django.db import migrations, models


def set_attendee_name_parts(apps, schema_editor):
    OrderPosition = apps.get_model('pretixbase', 'OrderPosition')  # noqa
    for op in OrderPosition.objects.exclude(attendee_name_cached=None).exclude(
            attendee_name_cached__isnull=True).iterator():
        op.attendee_name_parts = {'_legacy': op.attendee_name_cached}
        op.save(update_fields=['attendee_name_parts'])
    CartPosition = apps.get_model('pretixbase', 'CartPosition')  # noqa
    for op in CartPosition.objects.exclude(attendee_name_cached=None).exclude(
            attendee_name_cached__isnull=True).iterator():
        op.attendee_name_parts = {'_legacy': op.attendee_name_cached}
        op.save(update_fields=['attendee_name_parts'])
    InvoiceAddress = apps.get_model('pretixbase', 'InvoiceAddress')  # noqa
    for ia in InvoiceAddress.objects.exclude(name_cached=None).exclude(
            name_cached__isnull=True).iterator():
        ia.name_parts = {'_legacy': ia.name_cached}
        ia.save(update_fields=['name_parts'])


class Migration(migrations.Migration):
    dependencies = [
        ('pretixbase', '0101_auto_20181025_2255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartposition',
            old_name='attendee_name',
            new_name='attendee_name_cached',
        ),
        migrations.RenameField(
            model_name='orderposition',
            old_name='attendee_name',
            new_name='attendee_name_cached',
        ),
        migrations.RenameField(
            model_name='invoiceaddress',
            old_name='name',
            new_name='name_cached',
        ),
        migrations.AddField(
            model_name='cartposition',
            name='attendee_name_parts',
            field=models.JSONField(null=False, default=dict),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderposition',
            name='attendee_name_parts',
            field=models.JSONField(null=False, default=dict),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoiceaddress',
            name='name_parts',
            field=models.JSONField(default=dict),
            preserve_default=False,
        ),
        migrations.RunPython(set_attendee_name_parts, migrations.RunPython.noop)
    ]